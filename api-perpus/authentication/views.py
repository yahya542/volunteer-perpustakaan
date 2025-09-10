from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import Register, Login
from user.models import Profile
from authentication.serializers import RegisterSerializer, LoginSerializer, VerifyTokenSerializer
from django.core.mail import send_mail
from django.conf import settings
from drf_spectacular.utils import extend_schema
import random
from django.contrib.auth.hashers import check_password, make_password

class RegisterView(APIView):
    @extend_schema(
        summary="User Registration",
        description="Register a new user with NIK validation and email confirmation.",
        request=RegisterSerializer,
        responses={
            201: {"type": "object", "properties": {"message": {"type": "string"}}},
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    )
    def post(self, request):
        nik = request.data.get('nik', '')
        if len(nik) != 16:
            return Response({'error': 'NIK harus 16 digit'}, status=400)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            token = str(random.randint(100000, 999999))
            instance.verification_token = token
            instance.is_verified = False
            instance.save()
            # Create Login entry with hashed password
            Login.objects.create(
                nik=instance.nik,
                password=make_password(instance.password)
            )
            # Kirim email konfirmasi dengan token
            email = request.data.get('email')
            try:
                send_mail(
                    'Konfirmasi Akun Perpustakaan',
                    f'Terima kasih telah mendaftar. Token konfirmasi Anda: {token}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            return Response({'message': 'Registrasi berhasil. Silakan cek email untuk token konfirmasi.'}, status=201)
        


class VerifyTokenView(APIView):
    @extend_schema(
        summary="Verify User Token",
        description="Verify the token sent to email and activate the user account.",
        request=VerifyTokenSerializer,
        responses={
            200: {"type": "object", "properties": {"message": {"type": "string"}}},
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    )
    def post(self, request):
        serializer = VerifyTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        email = serializer.validated_data['email']
        token = serializer.validated_data['token']
        user = Register.objects.filter(email=email, verification_token=token, is_verified=False).first()
        if user:
            user.is_verified = True
            user.save()
            # Create Profile
            login_instance = Login.objects.get(nik=user.nik)
            Profile.objects.create(
                login=login_instance,
                username=user.username,
                email=user.email,
                nik=user.nik,
                phone=user.phone,
                address=user.address,
                tempat_lahir=user.tempat_lahir,
                tanggal_lahir=user.tanggal_lahir,
                institusi=user.institusi,
                keanggotaan=user.keanggotaan,
                jenis_kelamin=user.jenis_kelamin,
                foto_diri=user.foto_diri,
                foto_ktp=user.foto_ktp
            )
            return Response({'message': 'Akun berhasil diverifikasi. Profile telah dibuat. Anda dapat login sekarang.', 'next_step': 'POST /auth/login/ dengan nik dan password'}, status=200)
        return Response({'error': 'Token tidak valid atau akun sudah diverifikasi'}, status=400)


class LoginView(APIView):
    @extend_schema(
        summary="User Login",
        description="Authenticate user with NIK and password, check for admin role.",
        request=LoginSerializer,
        responses={
            200: {"type": "object", "properties": {"message": {"type": "string"}, "nik": {"type": "string"}}},
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    )

    def post(self, request):
        nik = request.data.get('nik')
        password = request.data.get('password')

        user = Login.objects.filter(nik=nik).first()
        print("DEBUG >>>")
        print("NIK input:", nik)
        print("Password input:", password)
        if user:
            print("Password di DB:", user.password)

        if user and check_password(password, user.password):
            # Check if user is verified
            register_user = Register.objects.filter(nik=nik, is_verified=True).first()
            if not register_user:
                return Response({'error': 'Akun belum diverifikasi. Silakan verifikasi email Anda.'}, status=400)
            if nik.startswith('ADM'):
                return Response({'message': 'Login admin berhasil', 'nik': nik}, status=200)
            else:
                return Response({'message': 'Login user berhasil', 'nik': nik}, status=200)
        return Response({'error': 'NIK atau password salah'}, status=400)


