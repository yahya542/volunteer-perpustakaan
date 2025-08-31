from rest_framework import serializers
from api.models import Register, Login

class RegisterSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Login
        fields = ['id', 'nik', 'password']