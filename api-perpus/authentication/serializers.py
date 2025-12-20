from rest_framework import serializers
from .models import User, UserGroup, GroupAccess, SystemLog
from user.models import Member
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
        model = User
        fields = '__all__'
        read_only_fields = ['user_id', 'input_date', 'last_update']
        extra_kwargs = {
            'passwd': {'write_only': True}
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