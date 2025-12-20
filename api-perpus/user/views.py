from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Member, MstMemberType, VisitorCount, Comment
from .serializers import MemberSerializer, MstMemberTypeSerializer, VisitorCountSerializer, CommentSerializer


class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Member read-only operations.

    Provides read-only functionality for library members including:
    - Listing all registered members
    - Retrieving individual member details
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# Constant member types data
MEMBER_TYPES_DATA = [
    {
        "member_type_id": 1,
        "member_type_name": "Mahasiswa",
        "loan_limit": 3,
        "loan_periode": 7,
        "enable_reserve": 1,
        "reserve_limit": 2,
        "member_periode": 365,
        "reborrow_limit": 2,
        "fine_each_day": 500,
        "grace_periode": 3,
        "input_date": "2025-09-17",
        "last_update": "2025-09-17"
    },
    {
        "member_type_id": 2,
        "member_type_name": "Dosen",
        "loan_limit": 5,
        "loan_periode": 14,
        "enable_reserve": 1,
        "reserve_limit": 5,
        "member_periode": 365,
        "reborrow_limit": 3,
        "fine_each_day": 1000,
        "grace_periode": 7,
        "input_date": "2025-09-17",
        "last_update": "2025-09-17"
    },
    {
        "member_type_id": 3,
        "member_type_name": "Staff",
        "loan_limit": 4,
        "loan_periode": 10,
        "enable_reserve": 1,
        "reserve_limit": 3,
        "member_periode": 365,
        "reborrow_limit": 2,
        "fine_each_day": 750,
        "grace_periode": 5,
        "input_date": "2025-09-17",
        "last_update": "2025-09-17"
    },
    {
        "member_type_id": 4,
        "member_type_name": "Umum",
        "loan_limit": 2,
        "loan_periode": 7,
        "enable_reserve": 0,
        "reserve_limit": 1,
        "member_periode": 180,
        "reborrow_limit": 1,
        "fine_each_day": 1000,
        "grace_periode": 3,
        "input_date": "2025-09-17",
        "last_update": "2025-09-17"
    }
]


class MstMemberTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Member Type operations.

    Provides read-only functionality for constant member types:
    - Listing all member types (constant data)
    - Retrieving individual member type details (constant data)

    Note: Member types are now constants and cannot be modified through the API.
    """
    serializer_class = MstMemberTypeSerializer

    def get_queryset(self):
        # Return constant data instead of database query
        return MEMBER_TYPES_DATA

    def list(self, request, *args, **kwargs):
        """Return constant member types data"""
        serializer = self.get_serializer(MEMBER_TYPES_DATA, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """Return specific member type from constant data"""
        member_type_id = int(kwargs['pk'])
        member_type = next((mt for mt in MEMBER_TYPES_DATA if mt['member_type_id'] == member_type_id), None)
        if member_type:
            serializer = self.get_serializer(member_type)
            return Response(serializer.data)
        return Response({'error': 'Member type not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        """Member types are constants and cannot be created"""
        return Response({'error': 'Member types are constants and cannot be modified'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        """Member types are constants and cannot be updated"""
        return Response({'error': 'Member types are constants and cannot be modified'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        """Member types are constants and cannot be partially updated"""
        return Response({'error': 'Member types are constants and cannot be modified'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        """Member types are constants and cannot be deleted"""
        return Response({'error': 'Member types are constants and cannot be modified'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class VisitorCountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Visitor Count read-only operations.

    Provides read-only functionality for visitor records including:
    - Listing all visitor check-ins
    - Retrieving individual visitor details
    """
    queryset = VisitorCount.objects.all()
    serializer_class = VisitorCountSerializer


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Comment read-only operations.

    Provides read-only functionality for user comments including:
    - Listing all user comments
    - Retrieving individual comment details
    - Getting bookmarks for a member
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @extend_schema(
        summary="Get bookmarked titles for a member",
        description="Retrieve all bookmarked titles (comments) for a specific member.",
        responses={
            200: CommentSerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def bookmarks(self, request, member_id=None):
        """Retrieve bookmarked titles for a specific member"""
        comments = Comment.objects.filter(member_id=member_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
