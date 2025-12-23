from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import (
    Biblio, LoanHistory, MstPublisher, MstAuthor, Loan
)
from .serializers import (
    BiblioSerializer, LoanHistorySerializer, PublisherSerializer, AuthorSerializer,
    DetailedBiblioSerializer, LoanSerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class BiblioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Bibliography operations.
    
    Provides read-only functionality for bibliographic records including:
    - Public read access (GET) for all users
    """
    queryset = Biblio.objects.all()
    serializer_class = BiblioSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # No authentication required for public access

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



class LoanHistoryViewSet(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        member_id = request.user.user_id  # atau relasi ke member

        loans = Loan.objects.filter(member_id=member_id)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)


class CurrentLoansViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Current Loans operations.
    
    Provides read-only functionality for current (active) loans including:
    - Listing all current loans for authenticated user
    - Filtering current loans for a specific member
    """
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for current loans
    authentication_classes = [JWTAuthentication]  # Explicitly require JWT authentication
    
    def get_queryset(self):
        """
        Filter loans to show only current/active loans (not returned yet)
        """
        # Get the member ID from the JWT token
        user = self.request.user
        if hasattr(user, 'member_id'):
            member_id = user.member_id
        else:
            # If we can't get member_id from user, return empty queryset
            return Loan.objects.none()
        
        # Filter for loans that belong to this member and haven't been returned
        # Loans that are not returned have is_return = 0 and return_date = NULL
        return Loan.objects.filter(
            member_id=member_id,
            is_return=0
        ).order_by('-loan_date')


# Let's add a separate view for the member loan history
from django.shortcuts import get_object_or_404

class MemberLoanHistoryView(APIView):
    """
    API endpoint for getting loan history for a specific member.
    """
    permission_classes = [IsAuthenticated]  # Require authentication for member loan history
    authentication_classes = [JWTAuthentication]  # Explicitly require JWT authentication
    
    @extend_schema(
        summary="Get loan history for a member (alternative endpoint)",
        description="Retrieve all loan history records for a specific member using a direct URL pattern.",
        responses={
            200: LoanHistorySerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def get(self, request, member_id):
        """Retrieve loan history for a specific member"""
        history = LoanHistory.objects.filter(member_id=member_id)
        serializer = LoanHistorySerializer(history, many=True)
        return Response(serializer.data)


class MemberCurrentLoansView(APIView):
    """
    API endpoint for getting current loans for a specific member.
    """
    permission_classes = [IsAuthenticated]  # Require authentication for member current loans
    authentication_classes = [JWTAuthentication]  # Explicitly require JWT authentication
    
    @extend_schema(
        summary="Get current loans for a member",
        description="Retrieve all current (active) loan records for a specific member.",
        responses={
            200: LoanSerializer(many=True),
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def get(self, request, member_id):
        """Retrieve current loans for a specific member"""
        # Filter for loans that belong to this member and haven't been returned
        current_loans = Loan.objects.filter(
            member_id=member_id,
            is_return=0
        ).order_by('-loan_date')
        serializer = LoanSerializer(current_loans, many=True)
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
    permission_classes = [AllowAny]
    authentication_classes = []  # No authentication required for public access


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Author read-only operations.
    
    Provides read-only functionality for authors including:
    - Listing all authors
    - Retrieving individual author details
    """
    queryset = MstAuthor.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # No authentication required for public access