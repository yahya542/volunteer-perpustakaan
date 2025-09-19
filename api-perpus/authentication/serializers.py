from rest_framework import serializers
from .models import User, UserGroup, GroupAccess, SystemLog
from user.models import Member, MstMemberType
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.Serializer):
    """
    Serializer for user registration with comprehensive member information.
    """
    # Basic information
    nama = serializers.CharField(max_length=100, help_text="Nama lengkap")
    nik = serializers.CharField(max_length=20, help_text="Nomor Induk Kependudukan (NIK)")
    tempat_lahir = serializers.CharField(max_length=100, required=False, help_text="Tempat lahir")
    tanggal_lahir = serializers.DateField(help_text="Tanggal lahir (YYYY-MM-DD)")
    institusi = serializers.CharField(max_length=200, required=False, help_text="Nama institusi")
    tipe_keanggotaan = serializers.CharField(max_length=20, help_text="Tipe keanggotaan")
    jenis_kelamin = serializers.ChoiceField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], help_text="Jenis kelamin")
    alamat = serializers.CharField(max_length=255, help_text="Alamat lengkap")
    nomor_hp = serializers.CharField(max_length=50, help_text="Nomor telepon")
    email = serializers.EmailField(help_text="Alamat email")
    password = serializers.CharField(write_only=True, min_length=6, help_text="Password")
    konfirmasi_password = serializers.CharField(write_only=True, help_text="Konfirmasi password")

    # File uploads - changed to CharField for optional text/file paths
    foto_diri = serializers.CharField(required=False, allow_blank=True, help_text="Path foto diri (opsional)")
    foto_ktp = serializers.CharField(required=False, allow_blank=True, help_text="Path foto KTP (opsional)")

    def validate(self, data):
        from user.models import Member

        # Validate password confirmation
        if data['password'] != data['konfirmasi_password']:
            raise serializers.ValidationError("Password dan konfirmasi password tidak cocok")

        # Validate membership type exists
        try:
            member_type = MstMemberType.objects.get(member_type_name=data['tipe_keanggotaan'])
            data['member_type_id'] = member_type.member_type_id
        except MstMemberType.DoesNotExist:
            raise serializers.ValidationError("Tipe keanggotaan tidak valid")

        # Validate NIK uniqueness
        if Member.objects.filter(member_id=data['nik']).exists():
            raise serializers.ValidationError("NIK sudah terdaftar dalam sistem")

        # Validate email uniqueness
        if Member.objects.filter(member_email=data['email']).exists():
            raise serializers.ValidationError("Email sudah terdaftar dalam sistem")

        # Validate username uniqueness (NIK as username)
        if User.objects.filter(username=data['nik']).exists():
            raise serializers.ValidationError("Username (NIK) sudah terdaftar dalam sistem")

        # Allow multiple verifications for the same email (user can request new token)
        # This allows users to register multiple times with the same email
        pass

        return data

    def create(self, validated_data):
        from datetime import date, timedelta
        from django.utils.crypto import get_random_string
        from django.utils import timezone
        from authentication.models import EmailVerification, User

        # Remove confirmation password from data
        validated_data.pop('konfirmasi_password')

        # Use provided NIK as member ID
        member_id = validated_data['nik']

        # Hash password for storage
        hashed_password = make_password(validated_data['password'])

        # Create member (but mark as pending verification)
        member = Member.objects.create(
            member_id=member_id,
            member_name=validated_data['nama'],
            gender=1 if validated_data['jenis_kelamin'] == 'L' else 2,
            birth_date=validated_data['tanggal_lahir'],
            birth_place=validated_data.get('tempat_lahir', ''),
            member_type_id=validated_data['member_type_id'],
            member_address=validated_data['alamat'],
            member_email=validated_data['email'],
            inst_name=validated_data.get('institusi', ''),
            member_phone=validated_data['nomor_hp'],
            member_image=validated_data.get('foto_diri', ''),
            ktp_image=validated_data.get('foto_ktp', ''),
            mpasswd=hashed_password,
            register_date=date.today(),
            expire_date=date.today().replace(year=date.today().year + 1),
            is_pending=1,  # Mark as pending verification
        )

        # Create User record immediately (but will be activated after verification)
        user = User.objects.create(
            username=member_id,  # Use NIK as username
            realname=validated_data['nama'],
            passwd=hashed_password,  # Use same hashed password
            email=validated_data['email'],
            user_type=2,  # 2 = member
        )

        # Generate 6-digit verification code (easier for manual input)
        import random
        token = str(random.randint(100000, 999999))  # 6-digit code
        expires_at = timezone.now() + timedelta(hours=24)  # Code expires in 24 hours

        # Create email verification record
        verification = EmailVerification.objects.create(
            email=validated_data['email'],
            token=token,
            member_id=member_id,
            expires_at=expires_at,
        )

        # Send verification email
        self.send_verification_email(validated_data['email'], token, validated_data['nama'])

        return member

    def send_verification_email(self, email, token, name):
        """Send verification email to user"""
        from django.core.mail import send_mail
        from django.conf import settings

        subject = 'Kode Verifikasi Akun Perpustakaan'
        message = f"""
        Halo {name},

        Terima kasih telah mendaftar di sistem perpustakaan kami.

        Kode verifikasi Anda: {token}

        Masukkan kode 6-digit di atas ke dalam aplikasi untuk mengaktifkan akun Anda.

        Atau klik link berikut untuk verifikasi otomatis:
        http://localhost:8000/auth/verify-token/?token={token}

        Kode ini akan kadaluarsa dalam 24 jam.

        Jika Anda tidak mendaftar, abaikan email ini.

        Terima kasih,
        Tim Perpustakaan
        """

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@library.com'),
                recipient_list=[email],
                fail_silently=False,
            )
            print(f"✅ Verification email sent successfully to {email}")
            print(f"📧 Please check your email inbox for the 6-digit verification code!")
            print(f"🔗 Direct verification link: http://localhost:8000/auth/verify-token/?token={token}")
            print(f"🔑 Verification Code: {token} (6 digits - for manual input)")
        except Exception as e:
            print(f"❌ Failed to send email to {email}: {e}")
            print(f"🔗 Use this code for manual verification: {token}")
            print(f"📝 POST to /auth/verify-token/ with: {{\"email\": \"{email}\", \"token\": \"{token}\"}}")


class VerifyTokenSerializer(serializers.Serializer):
    """
    Serializer for token verification.
    """
    email = serializers.EmailField()
    token = serializers.CharField(max_length=100)


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['user_id', 'input_date', 'last_update']
        extra_kwargs = {
            'passwd': {'write_only': True}
        }

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'
        read_only_fields = ['group_id', 'input_date', 'last_update']

class GroupAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAccess
        fields = '__all__'

class SystemLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemLog
        fields = '__all__'
        read_only_fields = ['log_id', 'log_date']