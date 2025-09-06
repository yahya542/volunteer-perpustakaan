from rest_framework import serializers
from authentication.models import Register, Login

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, help_text="User password")

    class Meta:
        model = Register
        fields = [
            'id',
            'username',
            'email',
            'password',
            'nik',
            'phone',
            'address',
            'date_joined',
        ]
        read_only_fields = ['date_joined']


class VerifyTokenSerializer(serializers.Serializer):
    """
    Serializer for token verification.
    """
    email = serializers.EmailField()
    token = serializers.CharField(max_length=100)


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer for user login.
    """
    password = serializers.CharField(write_only=True, help_text="User password")

    class Meta:
        model = Login
        fields = ['id', 'nik', 'password']