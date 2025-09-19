from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Member, MstMemberType, VisitorCount, Comment
from .serializers import MemberSerializer, MstMemberTypeSerializer, VisitorCountSerializer, CommentSerializer


@extend_schema_view(
    list=extend_schema(
        tags=['1. Anggota'],
        summary="Daftar semua anggota perpustakaan",
        description="Ambil daftar semua anggota perpustakaan yang terdaftar dengan detail mereka."
    ),
    retrieve=extend_schema(
        tags=['1. Anggota'],
        summary="Dapatkan detail anggota",
        description="Ambil informasi detail tentang anggota perpustakaan tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['1. Anggota'],
        summary="Daftarkan anggota baru",
        description="Daftarkan anggota perpustakaan baru dengan informasi pribadi dan kontak."
    ),
    update=extend_schema(
        tags=['1. Anggota'],
        summary="Perbarui anggota sepenuhnya",
        description="Perbarui semua field anggota perpustakaan yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['1. Anggota'],
        summary="Perbarui anggota sebagian",
        description="Perbarui field tertentu dari anggota perpustakaan yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['1. Anggota'],
        summary="Hapus anggota",
        description="Hapus anggota perpustakaan dari sistem secara permanen."
    ),
)
class MemberViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Member CRUD operations.

    Provides complete CRUD functionality for library members including:
    - Listing all registered members
    - Retrieving individual member details
    - Registering new members
    - Updating member information
    - Removing members
    - Member check-in functionality
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=True, methods=['post'])
    @extend_schema(
        summary="Member check-in",
        description="Record a member's visit to the library by creating a visitor count entry with their information.",
        responses={
            201: VisitorCountSerializer,
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def check_in(self, request, pk=None):
        """Record member check-in by creating a visitor count entry"""
        member = self.get_object()
        visitor = VisitorCount.objects.create(
            member_id=member.member_id,
            member_name=member.member_name,
            institution=member.inst_name
        )
        serializer = VisitorCountSerializer(visitor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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


@extend_schema_view(
    list=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Daftar semua tipe anggota",
        description="Ambil daftar semua tipe/kategori anggota yang tersedia di sistem perpustakaan. Data ini bersifat konstan dan tidak dapat diubah."
    ),
    retrieve=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Dapatkan detail tipe anggota",
        description="Ambil informasi detail tentang tipe anggota tertentu berdasarkan ID. Data ini bersifat konstan."
    ),
)
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


@extend_schema_view(
    list=extend_schema(
        tags=['1. Pengunjung'],
        summary="Daftar semua rekaman pengunjung",
        description="Ambil daftar semua rekaman pengunjung perpustakaan dengan informasi check-in."
    ),
    retrieve=extend_schema(
        tags=['1. Pengunjung'],
        summary="Dapatkan detail rekaman pengunjung",
        description="Ambil informasi detail tentang rekaman pengunjung tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['1. Pengunjung'],
        summary="Buat rekaman pengunjung baru",
        description="Buat rekaman pengunjung baru ketika anggota check-in ke perpustakaan."
    ),
    update=extend_schema(
        tags=['1. Pengunjung'],
        summary="Perbarui rekaman pengunjung sepenuhnya",
        description="Perbarui semua field rekaman pengunjung yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['1. Pengunjung'],
        summary="Perbarui rekaman pengunjung sebagian",
        description="Perbarui field tertentu dari rekaman pengunjung yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['1. Pengunjung'],
        summary="Hapus rekaman pengunjung",
        description="Hapus rekaman pengunjung dari sistem secara permanen."
    ),
)
class VisitorCountViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Visitor Count CRUD operations.

    Provides complete CRUD functionality for visitor records including:
    - Listing all visitor check-ins
    - Retrieving individual visitor details
    - Creating new visitor records
    - Updating existing visitor records
    - Deleting visitor records
    """
    queryset = VisitorCount.objects.all()
    serializer_class = VisitorCountSerializer


@extend_schema_view(
    list=extend_schema(
        tags=['1. Komentar'],
        summary="Daftar semua komentar",
        description="Ambil daftar semua komentar dan umpan balik pengguna di sistem."
    ),
    retrieve=extend_schema(
        tags=['Komentar'],
        summary="Dapatkan detail komentar",
        description="Ambil informasi detail tentang komentar tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['1. Komentar'],
        summary="Buat komentar baru",
        description="Buat entri komentar atau umpan balik baru dari pengguna."
    ),
    update=extend_schema(
        tags=['1. Komentar'],
        summary="Perbarui komentar sepenuhnya",
        description="Perbarui semua field komentar yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['1. Komentar'],
        summary="Perbarui komentar sebagian",
        description="Perbarui field tertentu dari komentar yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['1. Komentar'],
        summary="Hapus komentar",
        description="Hapus komentar dari sistem secara permanen."
    ),
)
class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Comment CRUD operations.

    Provides complete CRUD functionality for user comments including:
    - Listing all user comments
    - Retrieving individual comment details
    - Creating new comments
    - Updating existing comments
    - Deleting comments
    - Getting bookmarks for a member
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get'], url_path='bookmarks/(?P<member_id>[^/.]+)')
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
