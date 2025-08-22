from rest_framework import serializers
from .models import register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
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