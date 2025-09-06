from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import Register, Login
from authentication.serializers import RegisterSerializer,  LoginSerializer
from django.core.mail import send_mail
from django.conf import settings
from drf_spectacular.utils import extend_schema
import random

class RegisterView(APIView):
    @extend_schema(
        summary="User Registration",
        description="Register a new user with NIK validation and email confirmation.",
        request=RegisterSerializer,
        responses={
            201: RegisterSerializer,
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
            # Kirim email konfirmasi dengan token
            email = request.data.get('email')
            try:
                print("EMAIL_BACKEND setting:", settings.EMAIL_BACKEND)
                from django.core.mail import get_connection
                conn = get_connection()
                print("EMAIL_BACKEND actual class:", conn.__class__)

                send_mail(
                    'Konfirmasi Akun Perpustakaan',
                    f'Terima kasih telah mendaftar. Token konfirmasi Anda: {token}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            return Response(serializer.data, status=201)
        


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
        user = Login.objects.filter(nik=nik, password=password).first()
        if user:
            if nik.startswith('ADM'):
                return Response({'message': 'Login admin berhasil', 'nik': nik}, status=200)
            else:
                return Response({'message': 'Login user berhasil', 'nik': nik}, status=200)
        return Response({'error': 'NIK atau password salah'}, status=400)
