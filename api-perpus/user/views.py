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


@extend_schema_view(
    list=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Daftar semua tipe anggota",
        description="Ambil daftar semua tipe/kategori anggota yang tersedia di sistem perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Dapatkan detail tipe anggota",
        description="Ambil informasi detail tentang tipe anggota tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Buat tipe anggota baru",
        description="Buat tipe/kategori anggota baru untuk mengklasifikasikan anggota perpustakaan."
    ),
    update=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Perbarui tipe anggota sepenuhnya",
        description="Perbarui semua field tipe anggota yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Perbarui tipe anggota sebagian",
        description="Perbarui field tertentu dari tipe anggota yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['1. Tipe Anggota'],
        summary="Hapus tipe anggota",
        description="Hapus tipe anggota dari sistem secara permanen."
    ),
)
class MstMemberTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Member Type CRUD operations.

    Provides complete CRUD functionality for member types including:
    - Listing all member types
    - Retrieving individual member type details
    - Creating new member types
    - Updating existing member types
    - Deleting member types
    """
    queryset = MstMemberType.objects.all()
    serializer_class = MstMemberTypeSerializer


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
