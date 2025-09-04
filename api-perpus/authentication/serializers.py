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


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer for user login.
    """
    password = serializers.CharField(write_only=True, help_text="User password")

    class Meta:
        model = Login
        fields = ['id', 'nik', 'password']