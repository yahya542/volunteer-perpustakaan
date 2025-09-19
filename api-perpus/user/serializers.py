from rest_framework import serializers
from .models import Member, MstMemberType, VisitorCount, Comment

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['member_id', 'input_date', 'last_update']

class MstMemberTypeSerializer(serializers.Serializer):
    """
    Serializer for constant member type data.
    Since member types are now constants, we use a regular Serializer instead of ModelSerializer.
    """
    member_type_id = serializers.IntegerField(read_only=True)
    member_type_name = serializers.CharField(read_only=True)
    loan_limit = serializers.IntegerField(read_only=True)
    loan_periode = serializers.IntegerField(read_only=True)
    enable_reserve = serializers.IntegerField(read_only=True)
    reserve_limit = serializers.IntegerField(read_only=True)
    member_periode = serializers.IntegerField(read_only=True)
    reborrow_limit = serializers.IntegerField(read_only=True)
    fine_each_day = serializers.IntegerField(read_only=True)
    grace_periode = serializers.IntegerField(read_only=True)
    input_date = serializers.DateField(read_only=True)
    last_update = serializers.DateField(read_only=True)

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