from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import (
    Biblio, Item, Loan, Reserve, Fines, LoanHistory,
    MstGmd, MstLanguage, MstLocation, MstCollType, MstItemStatus,
    MstPublisher, MstPlace, MstSupplier, MstAuthor, MstTopic,
    MstFrequency, MstLoanRules, MstLabel, Setting
)
from .serializers import (
    BiblioSerializer, ItemSerializer, LoanSerializer, ReserveSerializer, FinesSerializer, LoanHistorySerializer,
    MstGmdSerializer, MstLanguageSerializer, MstLocationSerializer, MstCollTypeSerializer, MstItemStatusSerializer,
    MstPublisherSerializer, MstPlaceSerializer, MstSupplierSerializer, MstAuthorSerializer, MstTopicSerializer,
    MstFrequencySerializer, MstLoanRulesSerializer, MstLabelSerializer, SettingSerializer
)
from .permissions import ReadOnlyOrAuthenticated, LoanPermission, ReservePermission, FinePermission


@extend_schema_view(
    list=extend_schema(
        tags=['2. Bibliografi'],
        summary="Daftar semua rekaman bibliografi",
        description="Ambil daftar semua rekaman bibliografi dalam koleksi perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['2. Bibliografi'],
        summary="Dapatkan detail bibliografi",
        description="Ambil informasi detail tentang rekaman bibliografi tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['2. Bibliografi'],
        summary="Buat rekaman bibliografi baru",
        description="Buat rekaman bibliografi baru untuk buku atau publikasi di perpustakaan."
    ),
    update=extend_schema(
        tags=['2. Bibliografi'],
        summary="Perbarui bibliografi sepenuhnya",
        description="Perbarui semua field rekaman bibliografi yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['2. Bibliografi'],
        summary="Perbarui bibliografi sebagian",
        description="Perbarui field tertentu dari rekaman bibliografi yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['2. Bibliografi'],
        summary="Hapus rekaman bibliografi",
        description="Hapus rekaman bibliografi dari koleksi perpustakaan secara permanen."
    ),
)
class BiblioViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Bibliography CRUD operations.

    Provides complete CRUD functionality for bibliographic records including:
    - Listing all bibliographic entries
    - Retrieving individual bibliography details
    - Creating new bibliographic records
    - Updating existing records
    - Deleting bibliographic records
    - Retrieving associated items for a bibliography
    """
    queryset = Biblio.objects.all()
    serializer_class = BiblioSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

    @action(detail=True, methods=['get'])
    @extend_schema(
        summary="Get bibliography items",
        description="Retrieve all physical items/copies associated with a specific bibliographic record.",
        responses={
            200: ItemSerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def items(self, request, pk=None):
        """Retrieve all physical items associated with this bibliographic record"""
        biblio = self.get_object()
        items = Item.objects.filter(biblio_id=biblio.biblio_id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        tags=['2. Item'],
        summary="Daftar semua item perpustakaan",
        description="Ambil daftar semua item fisik/salinan dalam koleksi perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['2. Item'],
        summary="Dapatkan detail item",
        description="Ambil informasi detail tentang item perpustakaan tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['2. Item'],
        summary="Buat item perpustakaan baru",
        description="Buat item fisik/salinan baru untuk koleksi perpustakaan."
    ),
    update=extend_schema(
        tags=['2. Item'],
        summary="Perbarui item sepenuhnya",
        description="Perbarui semua field item perpustakaan yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['2. Item'],
        summary="Perbarui item sebagian",
        description="Perbarui field tertentu dari item perpustakaan yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['2. Item'],
        summary="Hapus item perpustakaan",
        description="Hapus item perpustakaan dari koleksi secara permanen."
    ),
)
class ItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Item CRUD operations.

    Provides complete CRUD functionality for library items including:
    - Listing all physical items
    - Retrieving individual item details
    - Creating new items
    - Updating existing items
    - Deleting items
    - Loaning items to members
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

    @action(detail=True, methods=['post'])
    @extend_schema(
        summary="Loan item to member",
        description="Create a loan record for this item to a specific member with loan and due dates.",
        request={
            "type": "object",
            "properties": {
                "member_id": {"type": "string", "description": "ID of the member borrowing the item"},
                "loan_date": {"type": "string", "format": "date", "description": "Date when the item is loaned"},
                "due_date": {"type": "string", "format": "date", "description": "Date when the item is due to be returned"}
            },
            "required": ["member_id"]
        },
        responses={
            201: LoanSerializer,
            400: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def loan(self, request, pk=None):
        """Create a loan record for this item to a member"""
        item = self.get_object()
        member_id = request.data.get('member_id')
        if not member_id:
            return Response({'error': 'member_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        loan = Loan.objects.create(
            item_code=item.item_code,
            member_id=member_id,
            loan_date=request.data.get('loan_date'),
            due_date=request.data.get('due_date')
        )
        serializer = LoanSerializer(loan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema_view(
    list=extend_schema(
        tags=['2. Peminjaman'],
        summary="Daftar semua rekaman peminjaman",
        description="Ambil daftar semua rekaman peminjaman aktif dan historis di perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['2. Peminjaman'],
        summary="Dapatkan detail peminjaman",
        description="Ambil informasi detail tentang rekaman peminjaman tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['2. Peminjaman'],
        summary="Buat rekaman peminjaman baru",
        description="Buat rekaman peminjaman baru ketika item dipinjam oleh anggota."
    ),
    update=extend_schema(
        tags=['2. Peminjaman'],
        summary="Perbarui peminjaman sepenuhnya",
        description="Perbarui semua field rekaman peminjaman yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['2. Peminjaman'],
        summary="Perbarui peminjaman sebagian",
        description="Perbarui field tertentu dari rekaman peminjaman yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['2. Peminjaman'],
        summary="Hapus rekaman peminjaman",
        description="Hapus rekaman peminjaman dari sistem secara permanen."
    ),
)
class LoanViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Loan CRUD operations.

    Provides complete CRUD functionality for loan records including:
    - Listing all loan transactions
    - Retrieving individual loan details
    - Creating new loan records
    - Updating existing loan records
    - Deleting loan records
    - Returning loaned items
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [LoanPermission]

    @action(detail=True, methods=['post'])
    @extend_schema(
        summary="Return loaned item",
        description="Mark a loaned item as returned by updating the return date and status.",
        request={
            "type": "object",
            "properties": {
                "return_date": {"type": "string", "format": "date", "description": "Date when the item was returned"}
            }
        },
        responses={
            200: LoanSerializer,
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def return_item(self, request, pk=None):
        """Mark the loaned item as returned"""
        loan = self.get_object()
        loan.is_return = 1
        loan.return_date = request.data.get('return_date')
        loan.save()
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='current/(?P<member_id>[^/.]+)')
    @extend_schema(
        summary="Get current loans for a member",
        description="Retrieve all current (unreturned) loan records for a specific member with book details.",
        responses={
            200: LoanSerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def current_loans(self, request, member_id=None):
        """Retrieve current loans for a specific member"""
        loans = Loan.objects.filter(member_id=member_id, is_return=0).select_related('item_code')
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        tags=['2. Reservasi'],
        summary="Daftar semua reservasi",
        description="Ambil daftar semua reservasi item yang dibuat oleh anggota perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['2. Reservasi'],
        summary="Dapatkan detail reservasi",
        description="Ambil informasi detail tentang reservasi tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['2. Reservasi'],
        summary="Buat reservasi baru",
        description="Buat reservasi baru untuk item oleh anggota perpustakaan."
    ),
    update=extend_schema(
        tags=['2. Reservasi'],
        summary="Perbarui reservasi sepenuhnya",
        description="Perbarui semua field reservasi yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['2. Reservasi'],
        summary="Perbarui reservasi sebagian",
        description="Perbarui field tertentu dari reservasi yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['2. Reservasi'],
        summary="Hapus reservasi",
        description="Hapus reservasi dari sistem secara permanen."
    ),
)
class ReserveViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Reservation CRUD operations.

    Provides complete CRUD functionality for item reservations including:
    - Listing all reservations
    - Retrieving individual reservation details
    - Creating new reservations
    - Updating existing reservations
    - Deleting reservations
    - Getting wishlist for a member
    """
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [ReservePermission]

    @action(detail=False, methods=['get'], url_path='wishlist/(?P<member_id>[^/.]+)')
    @extend_schema(
        summary="Get wishlist for a member",
        description="Retrieve all reserved items (wishlist) for a specific member.",
        responses={
            200: ReserveSerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def wishlist(self, request, member_id=None):
        """Retrieve wishlist (reservations) for a specific member"""
        reserves = Reserve.objects.filter(member_id=member_id)
        serializer = ReserveSerializer(reserves, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        tags=['2. Riwayat Peminjaman'],
        summary="Daftar semua rekaman riwayat peminjaman",
        description="Ambil daftar semua rekaman peminjaman historis di perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['2. Riwayat Peminjaman'],
        summary="Dapatkan detail riwayat peminjaman",
        description="Ambil informasi detail tentang rekaman riwayat peminjaman tertentu berdasarkan ID."
    ),
)
class LoanHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Loan History operations.

    Provides read-only functionality for loan history records including:
    - Listing all loan history
    - Retrieving individual loan history details
    - Getting loan history for a specific member
    """
    queryset = LoanHistory.objects.all()
    serializer_class = LoanHistorySerializer

    @action(detail=False, methods=['get'], url_path='member/(?P<member_id>[^/.]+)')
    @extend_schema(
        summary="Get loan history for a member",
        description="Retrieve all loan history records for a specific member.",
        responses={
            200: LoanHistorySerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def history(self, request, member_id=None):
        """Retrieve loan history for a specific member"""
        history = LoanHistory.objects.filter(member_id=member_id)
        serializer = LoanHistorySerializer(history, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        tags=['2. Denda'],
        summary="Daftar semua denda",
        description="Ambil daftar semua denda dan penalti yang dikenakan kepada anggota perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['2. Denda'],
        summary="Dapatkan detail denda",
        description="Ambil informasi detail tentang denda tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['2. Denda'],
        summary="Buat denda baru",
        description="Buat rekaman denda baru untuk anggota yang melanggar kebijakan perpustakaan."
    ),
    update=extend_schema(
        tags=['2. Denda'],
        summary="Perbarui denda sepenuhnya",
        description="Perbarui semua field rekaman denda yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['2. Denda'],
        summary="Perbarui denda sebagian",
        description="Perbarui field tertentu dari rekaman denda yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['2. Denda'],
        summary="Hapus rekaman denda",
        description="Hapus rekaman denda dari sistem secara permanen."
    ),
)
class FinesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Fines CRUD operations.

    Provides complete CRUD functionality for fine records including:
    - Listing all fines and penalties
    - Retrieving individual fine details
    - Creating new fine records
    - Updating existing fine records
    - Deleting fine records
    """
    queryset = Fines.objects.all()
    serializer_class = FinesSerializer
    permission_classes = [FinePermission]


# Master Data ViewSets
@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - GMD'],
        summary="Daftar semua tipe GMD",
        description="Ambil daftar semua tipe General Material Designation (GMD) yang digunakan untuk mengklasifikasikan publikasi."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - GMD'],
        summary="Dapatkan detail GMD",
        description="Ambil informasi detail tentang tipe GMD tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - GMD'],
        summary="Buat tipe GMD baru",
        description="Buat tipe General Material Designation baru untuk klasifikasi publikasi."
    ),
    update=extend_schema(
        tags=['3. Data Master - GMD'],
        summary="Perbarui GMD sepenuhnya",
        description="Perbarui semua field tipe GMD yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - GMD'],
        summary="Perbarui GMD sebagian",
        description="Perbarui field tertentu dari tipe GMD yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - GMD'],
        summary="Hapus tipe GMD",
        description="Hapus tipe GMD dari sistem secara permanen."
    ),
)
class MstGmdViewSet(viewsets.ModelViewSet):
    """
    ViewSet for GMD (General Material Designation) master data.

    Manages the classification of publication types such as books, journals, etc.
    """
    queryset = MstGmd.objects.all()
    serializer_class = MstGmdSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Bahasa'],
        summary="Daftar semua bahasa",
        description="Ambil daftar semua bahasa yang digunakan untuk katalog publikasi di perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Bahasa'],
        summary="Dapatkan detail bahasa",
        description="Ambil informasi detail tentang bahasa tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Bahasa'],
        summary="Buat bahasa baru",
        description="Buat entri bahasa baru untuk katalog publikasi."
    ),
    update=extend_schema(
        tags=['3. Data Master - Bahasa'],
        summary="Perbarui bahasa sepenuhnya",
        description="Perbarui semua field bahasa yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Bahasa'],
        summary="Perbarui bahasa sebagian",
        description="Perbarui field tertentu dari bahasa yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Bahasa'],
        summary="Hapus bahasa",
        description="Hapus bahasa dari sistem secara permanen."
    ),
)
class MstLanguageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Language master data.

    Manages the list of languages used for cataloging publications.
    """
    queryset = MstLanguage.objects.all()
    serializer_class = MstLanguageSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Lokasi'],
        summary="Daftar semua lokasi",
        description="Ambil daftar semua lokasi fisik tempat item disimpan di perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Lokasi'],
        summary="Dapatkan detail lokasi",
        description="Ambil informasi detail tentang lokasi tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Lokasi'],
        summary="Buat lokasi baru",
        description="Buat lokasi fisik baru untuk mengorganisir item perpustakaan."
    ),
    update=extend_schema(
        tags=['3. Data Master - Lokasi'],
        summary="Perbarui lokasi sepenuhnya",
        description="Perbarui semua field lokasi yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Lokasi'],
        summary="Perbarui lokasi sebagian",
        description="Perbarui field tertentu dari lokasi yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Lokasi'],
        summary="Hapus lokasi",
        description="Hapus lokasi dari sistem secara permanen."
    ),
)
class MstLocationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Location master data.

    Manages the physical locations where library items are stored.
    """
    queryset = MstLocation.objects.all()
    serializer_class = MstLocationSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Tipe Koleksi'],
        summary="Daftar semua tipe koleksi",
        description="Ambil daftar semua tipe koleksi yang digunakan untuk mengklasifikasikan materi perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Tipe Koleksi'],
        summary="Dapatkan detail tipe koleksi",
        description="Ambil informasi detail tentang tipe koleksi tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Tipe Koleksi'],
        summary="Buat tipe koleksi baru",
        description="Buat tipe koleksi baru untuk mengorganisir materi perpustakaan."
    ),
    update=extend_schema(
        tags=['3. Data Master - Tipe Koleksi'],
        summary="Perbarui tipe koleksi sepenuhnya",
        description="Perbarui semua field tipe koleksi yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Tipe Koleksi'],
        summary="Perbarui tipe koleksi sebagian",
        description="Perbarui field tertentu dari tipe koleksi yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Tipe Koleksi'],
        summary="Hapus tipe koleksi",
        description="Hapus tipe koleksi dari sistem secara permanen."
    ),
)
class MstCollTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Collection Type master data.

    Manages the types of collections in the library (e.g., reference, circulating, etc.).
    """
    queryset = MstCollType.objects.all()
    serializer_class = MstCollTypeSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Status Item'],
        summary="Daftar semua status item",
        description="Ambil daftar semua status yang mungkin untuk item perpustakaan (tersedia, dipinjam, rusak, dll.)."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Status Item'],
        summary="Dapatkan detail status item",
        description="Ambil informasi detail tentang status item tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Status Item'],
        summary="Buat status item baru",
        description="Buat tipe status baru untuk melacak kondisi item perpustakaan."
    ),
    update=extend_schema(
        tags=['3. Data Master - Status Item'],
        summary="Perbarui status item sepenuhnya",
        description="Perbarui semua field status item yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Status Item'],
        summary="Perbarui status item sebagian",
        description="Perbarui field tertentu dari status item yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Status Item'],
        summary="Hapus status item",
        description="Hapus status item dari sistem secara permanen."
    ),
)
class MstItemStatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Item Status master data.

    Manages the various statuses that library items can have.
    """
    queryset = MstItemStatus.objects.all()
    serializer_class = MstItemStatusSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Penerbit'],
        summary="Daftar semua penerbit",
        description="Ambil daftar semua penerbit yang terkait dengan materi perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Penerbit'],
        summary="Dapatkan detail penerbit",
        description="Ambil informasi detail tentang penerbit tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Penerbit'],
        summary="Buat penerbit baru",
        description="Buat entri penerbit baru untuk katalog publikasi."
    ),
    update=extend_schema(
        tags=['3. Data Master - Penerbit'],
        summary="Perbarui penerbit sepenuhnya",
        description="Perbarui semua field penerbit yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Penerbit'],
        summary="Perbarui penerbit sebagian",
        description="Perbarui field tertentu dari penerbit yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Penerbit'],
        summary="Hapus penerbit",
        description="Hapus penerbit dari sistem secara permanen."
    ),
)
class MstPublisherViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Publisher master data.

    Manages the publishers of library materials.
    """
    queryset = MstPublisher.objects.all()
    serializer_class = MstPublisherSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Tempat Terbit'],
        summary="Daftar semua tempat terbit",
        description="Ambil daftar semua tempat dimana publikasi diterbitkan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Tempat Terbit'],
        summary="Dapatkan detail tempat terbit",
        description="Ambil informasi detail tentang tempat terbit tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Tempat Terbit'],
        summary="Buat tempat terbit baru",
        description="Buat entri tempat baru untuk lokasi publikasi."
    ),
    update=extend_schema(
        tags=['3. Data Master - Tempat Terbit'],
        summary="Perbarui tempat terbit sepenuhnya",
        description="Perbarui semua field tempat terbit yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Tempat Terbit'],
        summary="Perbarui tempat terbit sebagian",
        description="Perbarui field tertentu dari tempat terbit yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Tempat Terbit'],
        summary="Hapus tempat terbit",
        description="Hapus tempat terbit dari sistem secara permanen."
    ),
)
class MstPlaceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Publication Place master data.

    Manages the places where publications were published.
    """
    queryset = MstPlace.objects.all()
    serializer_class = MstPlaceSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Supplier'],
        summary="Daftar semua supplier",
        description="Ambil daftar semua supplier yang menyediakan materi ke perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Supplier'],
        summary="Dapatkan detail supplier",
        description="Ambil informasi detail tentang supplier tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Supplier'],
        summary="Buat supplier baru",
        description="Buat entri supplier baru untuk pengadaan materi perpustakaan."
    ),
    update=extend_schema(
        tags=['3. Data Master - Supplier'],
        summary="Perbarui supplier sepenuhnya",
        description="Perbarui semua field supplier yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Supplier'],
        summary="Perbarui supplier sebagian",
        description="Perbarui field tertentu dari supplier yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Supplier'],
        summary="Hapus supplier",
        description="Hapus supplier dari sistem secara permanen."
    ),
)
class MstSupplierViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Supplier master data.

    Manages the suppliers of library materials.
    """
    queryset = MstSupplier.objects.all()
    serializer_class = MstSupplierSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Penulis'],
        summary="Daftar semua penulis",
        description="Ambil daftar semua penulis yang terkait dengan materi perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Penulis'],
        summary="Dapatkan detail penulis",
        description="Ambil informasi detail tentang penulis tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Penulis'],
        summary="Buat penulis baru",
        description="Buat entri penulis baru untuk katalog publikasi."
    ),
    update=extend_schema(
        tags=['3. Data Master - Penulis'],
        summary="Perbarui penulis sepenuhnya",
        description="Perbarui semua field penulis yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Penulis'],
        summary="Perbarui penulis sebagian",
        description="Perbarui field tertentu dari penulis yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Penulis'],
        summary="Hapus penulis",
        description="Hapus penulis dari sistem secara permanen."
    ),
)
class MstAuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Author master data.

    Manages the authors of library materials.
    """
    queryset = MstAuthor.objects.all()
    serializer_class = MstAuthorSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Topik'],
        summary="Daftar semua topik",
        description="Ambil daftar semua topik subjek untuk mengklasifikasikan materi perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Topik'],
        summary="Dapatkan detail topik",
        description="Ambil informasi detail tentang topik tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Topik'],
        summary="Buat topik baru",
        description="Buat topik subjek baru untuk klasifikasi materi."
    ),
    update=extend_schema(
        tags=['3. Data Master - Topik'],
        summary="Perbarui topik sepenuhnya",
        description="Perbarui semua field topik yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Topik'],
        summary="Perbarui topik sebagian",
        description="Perbarui field tertentu dari topik yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Topik'],
        summary="Hapus topik",
        description="Hapus topik dari sistem secara permanen."
    ),
)
class MstTopicViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Topic master data.

    Manages the subject topics for classifying library materials.
    """
    queryset = MstTopic.objects.all()
    serializer_class = MstTopicSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Frekuensi'],
        summary="Daftar semua frekuensi publikasi",
        description="Ambil daftar semua frekuensi publikasi (harian, mingguan, bulanan, dll.)."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Frekuensi'],
        summary="Dapatkan detail frekuensi",
        description="Ambil informasi detail tentang frekuensi publikasi tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Frekuensi'],
        summary="Buat frekuensi baru",
        description="Buat frekuensi publikasi baru untuk periodik."
    ),
    update=extend_schema(
        tags=['3. Data Master - Frekuensi'],
        summary="Perbarui frekuensi sepenuhnya",
        description="Perbarui semua field frekuensi yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Frekuensi'],
        summary="Perbarui frekuensi sebagian",
        description="Perbarui field tertentu dari frekuensi yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Frekuensi'],
        summary="Hapus frekuensi",
        description="Hapus frekuensi publikasi dari sistem secara permanen."
    ),
)
class MstFrequencyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Publication Frequency master data.

    Manages the frequencies at which publications are issued.
    """
    queryset = MstFrequency.objects.all()
    serializer_class = MstFrequencySerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Aturan Peminjaman'],
        summary="Daftar semua aturan peminjaman",
        description="Ambil daftar semua aturan peminjaman yang mendefinisikan kebijakan peminjaman."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Aturan Peminjaman'],
        summary="Dapatkan detail aturan peminjaman",
        description="Ambil informasi detail tentang aturan peminjaman tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Aturan Peminjaman'],
        summary="Buat aturan peminjaman baru",
        description="Buat aturan peminjaman baru yang mendefinisikan kebijakan dan batas peminjaman."
    ),
    update=extend_schema(
        tags=['3. Data Master - Aturan Peminjaman'],
        summary="Perbarui aturan peminjaman sepenuhnya",
        description="Perbarui semua field aturan peminjaman yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Aturan Peminjaman'],
        summary="Perbarui aturan peminjaman sebagian",
        description="Perbarui field tertentu dari aturan peminjaman yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Aturan Peminjaman'],
        summary="Hapus aturan peminjaman",
        description="Hapus aturan peminjaman dari sistem secara permanen."
    ),
)
class MstLoanRulesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Loan Rules master data.

    Manages the rules governing loan policies and borrowing limits.
    """
    queryset = MstLoanRules.objects.all()
    serializer_class = MstLoanRulesSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Data Master - Label'],
        summary="Daftar semua label",
        description="Ambil daftar semua label yang digunakan untuk mengorganisir materi perpustakaan."
    ),
    retrieve=extend_schema(
        tags=['3. Data Master - Label'],
        summary="Dapatkan detail label",
        description="Ambil informasi detail tentang label tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Data Master - Label'],
        summary="Buat label baru",
        description="Buat label baru untuk mengorganisir dan mengkategorikan materi."
    ),
    update=extend_schema(
        tags=['3. Data Master - Label'],
        summary="Perbarui label sepenuhnya",
        description="Perbarui semua field label yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Data Master - Label'],
        summary="Perbarui label sebagian",
        description="Perbarui field tertentu dari label yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Data Master - Label'],
        summary="Hapus label",
        description="Hapus label dari sistem secara permanen."
    ),
)
class MstLabelViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Label master data.

    Manages the labels used for organizing library materials.
    """
    queryset = MstLabel.objects.all()
    serializer_class = MstLabelSerializer

@extend_schema_view(
    list=extend_schema(
        tags=['3. Pengaturan Sistem'],
        summary="Daftar semua pengaturan sistem",
        description="Ambil daftar semua pengaturan konfigurasi sistem."
    ),
    retrieve=extend_schema(
        tags=['3. Pengaturan Sistem'],
        summary="Dapatkan detail pengaturan sistem",
        description="Ambil informasi detail tentang pengaturan sistem tertentu berdasarkan ID."
    ),
    create=extend_schema(
        tags=['3. Pengaturan Sistem'],
        summary="Buat pengaturan sistem baru",
        description="Buat pengaturan konfigurasi sistem baru."
    ),
    update=extend_schema(
        tags=['3. Pengaturan Sistem'],
        summary="Perbarui pengaturan sistem sepenuhnya",
        description="Perbarui semua field pengaturan sistem yang ada dengan data baru."
    ),
    partial_update=extend_schema(
        tags=['3. Pengaturan Sistem'],
        summary="Perbarui pengaturan sistem sebagian",
        description="Perbarui field tertentu dari pengaturan sistem yang ada tanpa mempengaruhi field lain."
    ),
    destroy=extend_schema(
        tags=['3. Pengaturan Sistem'],
        summary="Hapus pengaturan sistem",
        description="Hapus pengaturan sistem dari sistem secara permanen."
    ),
)
class SettingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for System Settings.

    Manages the configuration settings for the library management system.
    """
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer