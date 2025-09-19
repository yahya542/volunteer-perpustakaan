from rest_framework import serializers
from .models import Member, MstMemberType, VisitorCount, Comment

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['member_id', 'input_date', 'last_update']

class MstMemberTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMemberType
        fields = '__all__'
        read_only_fields = ['input_date', 'last_update']

class VisitorCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorCount
        fields = '__all__'
        read_only_fields = ['visitor_id', 'checkin_date']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['comment_id', 'input_date', 'last_update']