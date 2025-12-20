from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import (
    Biblio, LoanHistory, MstPublisher, MstAuthor
)
from .serializers import (
    BiblioSerializer, LoanHistorySerializer,
    DetailedBiblioSerializer, PublisherSerializer, AuthorSerializer
)
from .permissions import ReadOnlyOrAuthenticated


class BiblioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Bibliography read-only operations.
    
    Provides read-only functionality for bibliographic records including:
    - Listing all bibliographic entries
    - Retrieving individual bibliography details with related information
    """
    queryset = Biblio.objects.all()
    serializer_class = BiblioSerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    
    def get_serializer_class(self):
        # Use DetailedBiblioSerializer for retrieve action or when include_related param is present
        if self.action == 'retrieve' or self.request.query_params.get('include_related'):
            return DetailedBiblioSerializer
        return BiblioSerializer

    @action(detail=True, methods=['get'], url_path='detailed')
    @extend_schema(
        summary="Get detailed bibliography with related data",
        description="Retrieve comprehensive bibliographic record with all related information including authors, publisher, language, etc.",
        responses={
            200: DetailedBiblioSerializer,
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def detailed(self, request, pk=None):
        """Retrieve detailed bibliographic record with all related information"""
        biblio = self.get_object()
        serializer = DetailedBiblioSerializer(biblio)
        return Response(serializer.data)


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


class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Publisher read-only operations.
    
    Provides read-only functionality for publishers including:
    - Listing all publishers
    - Retrieving individual publisher details
    """
    queryset = MstPublisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [ReadOnlyOrAuthenticated]


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Author read-only operations.
    
    Provides read-only functionality for authors including:
    - Listing all authors
    - Retrieving individual author details
    """
    queryset = MstAuthor.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [ReadOnlyOrAuthenticated]