from rest_framework import serializers
from user.models import Member
from .models import UserGroup, GroupAccess, SystemLog
from django.contrib.auth.hashers import make_password



class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)


class RefreshTokenSerializer(serializers.Serializer):
    """
    Serializer for refreshing tokens with email and password.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['input_date', 'last_update']
        extra_kwargs = {
            'mpasswd': {'write_only': True}
        }


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'
        read_only_fields = ['group_id', 'input_date', 'last_update']


class GroupAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAccess
        fields = '__all__'


class SystemLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemLog
        fields = '__all__'
        read_only_fields = ['log_id', 'log_date']