from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, UserGroup, GroupAccess, SystemLog
from user.models import Member
from .serializers import (
    LoginSerializer, RefreshTokenSerializer, UserSerializer, UserGroupSerializer, GroupAccessSerializer, SystemLogSerializer
)
from django.contrib.auth.hashers import check_password




class LoginView(APIView):
    """
    API endpoint for user authentication.

    Authenticates users by verifying their username and password against
    the stored credentials. Returns success message with username on
    successful authentication.
    """
    @extend_schema(
        summary="User Login",
        description="Authenticate user by verifying username and password. Returns JWT tokens for authenticated requests.",
        request=LoginSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                    "username": {"type": "string"},
                    "user_type": {"type": "integer"},
                    "access_token": {"type": "string"},
                    "refresh_token": {"type": "string"},
                    "token_type": {"type": "string"},
                    "expires_in": {"type": "integer"}
                }
            },
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    )

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()
        if user and check_password(password, user.passwd):
            # Check if member account is active (not pending verification)
            try:
                member = Member.objects.get(member_id=username)
                if member.is_pending == 1:
                    return Response({'error': 'Account belum diverifikasi. Silakan verifikasi email Anda terlebih dahulu.'}, status=400)
            except Member.DoesNotExist:
                return Response({'error': 'Data member tidak ditemukan'}, status=400)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'message': 'Login successful',
                'username': username,
                'user_type': user.user_type,
                'access_token': access_token,
                'refresh_token': refresh_token,
                'token_type': 'Bearer',
                'expires_in': 3600  # 1 hour
            }, status=200)
        return Response({'error': 'Invalid credentials or account not verified'}, status=400)


class RefreshTokenView(APIView):
    """
    API endpoint for refreshing tokens with email and password.
    
    Authenticates users by verifying their email and password against
    the stored credentials. Returns new JWT tokens for authenticated requests.
    """
    @extend_schema(
        summary="Refresh User Token",
        description="Authenticate user by verifying email and password. Returns new JWT tokens for authenticated requests.",
        request=RefreshTokenSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                    "username": {"type": "string"},
                    "user_type": {"type": "integer"},
                    "access_token": {"type": "string"},
                    "refresh_token": {"type": "string"},
                    "token_type": {"type": "string"},
                    "expires_in": {"type": "integer"}
                }
            },
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    )

    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
            
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # Find user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=400)

        # Verify password
        if not check_password(password, user.passwd):
            return Response({'error': 'Invalid credentials'}, status=400)

        # Check if member account is active (not pending verification)
        try:
            member = Member.objects.get(member_id=user.username)
            if member.is_pending == 1:
                return Response({'error': 'Account belum diverifikasi. Silakan verifikasi email Anda terlebih dahulu.'}, status=400)
        except Member.DoesNotExist:
            return Response({'error': 'Data member tidak ditemukan'}, status=400)

        # Generate new JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'message': 'Token refreshed successfully',
            'username': user.username,
            'user_type': user.user_type,
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_type': 'Bearer',
            'expires_in': 3600  # 1 hour
        }, status=200)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for User read-only operations.

    Provides read-only functionality for system users including:
    - Listing all users
    - Retrieving individual user details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for User Group read-only operations.

    Provides read-only functionality for user groups including:
    - Listing all user groups
    - Retrieving individual user group details
    """
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


class GroupAccessViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Group Access read-only operations.

    Provides read-only functionality for group access permissions including:
    - Listing all group access permissions
    - Retrieving individual group access permission details
    """
    queryset = GroupAccess.objects.all()
    serializer_class = GroupAccessSerializer


class SystemLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for System Log read-only operations.

    Provides read-only access to system logs including:
    - Listing all system logs
    - Retrieving individual system log details
    """
    queryset = SystemLog.objects.all()
    serializer_class = SystemLogSerializer