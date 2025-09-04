from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication.models import Register, Login
from authentication.serializers import RegisterSerializer,  LoginSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema, extend_schema_view

@csrf_exempt
@api_view(['GET', 'POST'])
@extend_schema_view(
    POST=extend_schema(
        summary="User Registration",
        description="Register a new user with NIK validation and email confirmation.",
        request=RegisterSerializer,
        responses={
            201: RegisterSerializer,
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    ),
    GET=extend_schema(
        summary="List Registrations",
        description="List all user registrations.",
        responses={200: RegisterSerializer(many=True)},
    ),
)
def register(request):
    """
    Handle user registration.

    GET: List all registered users.
    POST: Register a new user with NIK validation and email confirmation.
    """
    if request.method == 'GET':
        queryset = Register.objects.all()
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        nik = request.data.get('nik', '')
        if len(nik) != 16:
            return Response({'error': 'NIK harus 16 digit'}, status=400)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            nik = instance.nik
            id_str = str(instance.id)
            token = f"420{nik[-2:]}{id_str[-2:]}"
            # Kirim email konfirmasi dengan token
            email = request.data.get('email')
            send_mail(
                'Konfirmasi Akun Perpustakaan',
                f'Terima kasih telah mendaftar. Token konfirmasi Anda: {token}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return Response(serializer.data, status=201)
        


@api_view(['GET', 'POST'])
@extend_schema(
    methods=['POST'],
    summary="User Login",
    description="Authenticate user with NIK and password, check for admin role.",
    request=LoginSerializer,
    responses={
        200: {"type": "object", "properties": {"message": {"type": "string"}, "nik": {"type": "string"}}},
        400: {"type": "object", "properties": {"error": {"type": "string"}}}
    },
)
@extend_schema(
    methods=['GET'],
    summary="List Logins",
    description="List all login records.",
    responses={200: LoginSerializer(many=True)},
)
def login(request):
    """
    Handle user login.

    GET: List all login records.
    POST: Authenticate user with NIK and password, check for admin role.
    """
    if request.method == 'GET':
        queryset = Login.objects.all()
        serializer = LoginSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        nik = request.data.get('nik')
        password = request.data.get('password')
        user = Login.objects.filter(nik=nik, password=password).first()
        if user:
            if nik.startswith('ADM'):
                return Response({'message': 'Login admin berhasil', 'nik': nik}, status=200)
            else:
                return Response({'message': 'Login user berhasil', 'nik': nik}, status=200)
        return Response({'error': 'NIK atau password salah'}, status=400)
