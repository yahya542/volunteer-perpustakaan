from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, UserGroup, GroupAccess, SystemLog
from user.models import Member
from .serializers import (
    RegisterSerializer, LoginSerializer, VerifyTokenSerializer,
    UserSerializer, UserGroupSerializer, GroupAccessSerializer, SystemLogSerializer
)
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.hashers import check_password, make_password

class RegisterView(APIView):
    """
    API endpoint for user registration.

    Allows new users to create an account by providing their username, real name,
    email, and password. The password is securely hashed before storage.
    """
    @extend_schema(
        summary="User Registration",
        description="Register a new user account with username, real name, email, and password. Password is securely hashed before storage.",
        request=RegisterSerializer,
        responses={
            201: {"type": "object", "properties": {"message": {"type": "string"}}},
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # The serializer's create method will handle creating both Member and User
            member = serializer.save()
            return Response({'message': 'User created successfully'}, status=201)
        return Response(serializer.errors, status=400)


class VerifyTokenView(APIView):
    """
    API endpoint for email token verification.

    Verifies tokens sent to user emails for account verification purposes.
    Upon successful verification, creates User record and activates member account.
    """
    @extend_schema(
        summary="Verify User Token",
        description="Verify the token sent to user's email for account verification. Creates User record and activates member account upon successful verification.",
        request=VerifyTokenSerializer,
        responses={
            200: {"type": "object", "properties": {"message": {"type": "string"}}},
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
    )
    def post(self, request):
        from authentication.models import EmailVerification
        from django.contrib.auth.hashers import make_password
        from user.models import Member

        serializer = VerifyTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        email = serializer.validated_data['email']
        token = serializer.validated_data['token']

        try:
            # Find verification record
            verification = EmailVerification.objects.get(
                email=email,
                token=token,
                is_used=False
            )

            # Check if token is expired
            if verification.is_expired():
                return Response({'error': 'Token has expired'}, status=400)

            # Find member record
            try:
                member = Member.objects.get(member_id=verification.member_id)
            except Member.DoesNotExist:
                return Response({'error': 'Member record not found'}, status=400)

            # Check if member is already verified
            if member.is_pending == 0:
                return Response({'error': 'Account already verified and active'}, status=400)

            # Get the User record (should exist from registration)
            try:
                user = User.objects.get(username=verification.member_id)
            except User.DoesNotExist:
                return Response({'error': 'User account not found. Please contact administrator.'}, status=400)

            # Update member status to active
            member.is_pending = 0
            member.save()

            # Mark verification as used
            verification.is_used = True
            verification.save()

            return Response({
                'message': 'Email verified successfully! Your account is now active.',
                'member_id': verification.member_id,
                'username': verification.member_id
            }, status=200)

        except EmailVerification.DoesNotExist:
            return Response({'error': 'Invalid token or email'}, status=400)
        except Exception as e:
            return Response({'error': f'Verification failed: {str(e)}'}, status=400)


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



@extend_schema_view(
    list=extend_schema(
        tags=['4. System Users'],
        summary="List all system users",
        description="Retrieve a list of all users in the system with their details."
    ),
    retrieve=extend_schema(
        tags=['4. System Users'],
        summary="Get user details",
        description="Retrieve detailed information about a specific user by their ID."
    ),
    create=extend_schema(
        tags=['4. System Users'],
        summary="Create new user",
        description="Create a new system user with the provided information."
    ),
    update=extend_schema(
        tags=['4. System Users'],
        summary="Update user completely",
        description="Update all fields of an existing user with new data."
    ),
    partial_update=extend_schema(
        tags=['4. System Users'],
        summary="Update user partially",
        description="Update specific fields of an existing user without affecting other fields."
    ),
    destroy=extend_schema(
        tags=['4. System Users'],
        summary="Delete user",
        description="Remove a user from the system permanently."
    ),
)
class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User CRUD operations.

    Provides complete CRUD functionality for system users including:
    - Listing all users
    - Retrieving individual user details
    - Creating new users
    - Updating existing users
    - Deleting users
    - Changing user passwords
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    @extend_schema(
        summary="Change user password",
        description="Change the password for a specific user. Requires the old password for verification.",
        request={
            "type": "object",
            "properties": {
                "old_password": {"type": "string", "description": "Current password for verification"},
                "new_password": {"type": "string", "description": "New password to set"}
            },
            "required": ["old_password", "new_password"]
        },
        responses={
            200: {"type": "object", "properties": {"message": {"type": "string"}}},
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def change_password(self, request, pk=None):
        """Change user password"""
        user = self.get_object()
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not check_password(old_password, user.passwd):
            return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        user.passwd = make_password(new_password)
        user.save()
        return Response({'message': 'Password changed successfully'})


@extend_schema_view(
    list=extend_schema(
        tags=['4. User Groups'],
        summary="List all user groups",
        description="Retrieve a list of all user groups in the system."
    ),
    retrieve=extend_schema(
        tags=['4. User Groups'],
        summary="Get user group details",
        description="Retrieve detailed information about a specific user group by its ID."
    ),
    create=extend_schema(
        tags=['4. User Groups'],
        summary="Create new user group",
        description="Create a new user group with the provided information."
    ),
    update=extend_schema(
        tags=['4. User Groups'],
        summary="Update user group completely",
        description="Update all fields of an existing user group with new data."
    ),
    partial_update=extend_schema(
        tags=['4. User Groups'],
        summary="Update user group partially",
        description="Update specific fields of an existing user group without affecting other fields."
    ),
    destroy=extend_schema(
        tags=['4. User Groups'],
        summary="Delete user group",
        description="Remove a user group from the system permanently."
    ),
)
class UserGroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User Group CRUD operations.

    Provides complete CRUD functionality for user groups including:
    - Listing all user groups
    - Retrieving individual user group details
    - Creating new user groups
    - Updating existing user groups
    - Deleting user groups
    """
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


@extend_schema_view(
    list=extend_schema(
        tags=['4. Group Access'],
        summary="List all group access permissions",
        description="Retrieve a list of all group access permissions in the system."
    ),
    retrieve=extend_schema(
        tags=['4. Group Access'],
        summary="Get group access details",
        description="Retrieve detailed information about a specific group access permission by its ID."
    ),
    create=extend_schema(
        tags=['4. Group Access'],
        summary="Create new group access permission",
        description="Create a new group access permission with the provided information."
    ),
    update=extend_schema(
        tags=['4. Group Access'],
        summary="Update group access completely",
        description="Update all fields of an existing group access permission with new data."
    ),
    partial_update=extend_schema(
        tags=['4. Group Access'],
        summary="Update group access partially",
        description="Update specific fields of an existing group access permission without affecting other fields."
    ),
    destroy=extend_schema(
        tags=['4. Group Access'],
        summary="Delete group access permission",
        description="Remove a group access permission from the system permanently."
    ),
)
class GroupAccessViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Group Access CRUD operations.

    Provides complete CRUD functionality for group access permissions including:
    - Listing all group access permissions
    - Retrieving individual group access details
    - Creating new group access permissions
    - Updating existing group access permissions
    - Deleting group access permissions
    """
    queryset = GroupAccess.objects.all()
    serializer_class = GroupAccessSerializer


@extend_schema_view(
    list=extend_schema(
        tags=['4. System Logs'],
        summary="List all system logs",
        description="Retrieve a list of all system log entries for auditing and monitoring purposes."
    ),
    retrieve=extend_schema(
        tags=['4. System Logs'],
        summary="Get system log details",
        description="Retrieve detailed information about a specific system log entry by its ID."
    ),
    create=extend_schema(
        tags=['4. System Logs'],
        summary="Create new system log entry",
        description="Create a new system log entry to record system activities."
    ),
    update=extend_schema(
        tags=['4. System Logs'],
        summary="Update system log completely",
        description="Update all fields of an existing system log entry with new data."
    ),
    partial_update=extend_schema(
        tags=['4. System Logs'],
        summary="Update system log partially",
        description="Update specific fields of an existing system log entry without affecting other fields."
    ),
    destroy=extend_schema(
        tags=['4. System Logs'],
        summary="Delete system log entry",
        description="Remove a system log entry from the system permanently."
    ),
)
class SystemLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for System Log CRUD operations.

    Provides complete CRUD functionality for system logs including:
    - Listing all system log entries
    - Retrieving individual log details
    - Creating new log entries
    - Updating existing log entries
    - Deleting log entries
    """
    queryset = SystemLog.objects.all()
    serializer_class = SystemLogSerializer
