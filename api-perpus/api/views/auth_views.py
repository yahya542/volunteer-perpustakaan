from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Register, Login
from api.serializers.auth_serializers import RegisterSerializer,  LoginSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
def register(request):
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
def login(request):
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
