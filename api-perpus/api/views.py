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
from .authentication import MemberJWTAuthentication
from django.core.mail import send_mail
from django.conf import settings
import re


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



class LoanHistoryView(APIView):
    authentication_classes = [MemberJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Get loan history for current user",
        description="Retrieve all loan history records for the currently authenticated user based on their JWT token.",
        responses={
            200: LoanHistorySerializer(many=True),
            401: {"type": "object", "properties": {"detail": {"type": "string"}}}
        }
    )
    def get(self, request):
        member_id = request.user.user_id  # Get member_id from JWT token
        
        # Get loan history for the current user
        history = LoanHistory.objects.filter(member_id=member_id)
        serializer = LoanHistorySerializer(history, many=True)
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
    authentication_classes = [MemberJWTAuthentication]  # Use custom JWT authentication
    
    def get_queryset(self):
        """
        Filter loans to show only current/active loans (not returned yet)
        """
        # Get the member ID from the JWT token
        user = self.request.user
        if hasattr(user, 'user_id'):
            member_id = user.user_id
        elif hasattr(user, 'member_id'):
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
    authentication_classes = [MemberJWTAuthentication]  # Use custom JWT authentication
    
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
        # Query loan history for the specified member_id
        history = LoanHistory.objects.filter(member_id=member_id)
        
        serializer = LoanHistorySerializer(history, many=True)
        return Response(serializer.data)


class MemberCurrentLoansView(APIView):
    """
    API endpoint for getting current loans for a specific member.
    """
    permission_classes = [IsAuthenticated]  # Require authentication for member current loans
    authentication_classes = [MemberJWTAuthentication]  # Use custom JWT authentication
    
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


class LoanExtensionRequestView(APIView):
    """
    API endpoint for requesting loan extension with WhatsApp notification to admin.
    
    This view handles loan extension requests where the user provides:
    - loan_id: The ID of the loan to extend
    - whatsapp_number: The WhatsApp number where they can be contacted
    
    The system validates the loan belongs to the user, then sends an email
    to admin requesting the extension with the provided WhatsApp number.
    """
    authentication_classes = [MemberJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Request loan extension with WhatsApp notification",
        description="Submit a loan extension request with WhatsApp number for admin contact.",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "loan_id": {
                        "type": "integer",
                        "example": 1
                    },
                    "whatsapp_number": {
                        "type": "string",
                        "example": "628123456789"
                    }
                },
                "required": ["whatsapp_number"]
            }
        },
        responses={
            200: {"type": "object", "properties": {"message": {"type": "string"}}},
            400: {"type": "object", "properties": {"error": {"type": "string"}}},
            401: {"type": "object", "properties": {"detail": {"type": "string"}}},
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    def post(self, request):
        # Extract whatsapp_number from request
        whatsapp_number = request.data.get('whatsapp_number')
        
        # Validate input data
        if not whatsapp_number:
            return Response(
                {'error': 'whatsapp_number is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validate WhatsApp number format
        if not self.is_valid_whatsapp_number(whatsapp_number):
            return Response(
                {'error': 'Invalid WhatsApp number format. Use format like 628123456789'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get the authenticated user's member_id from JWT token
        member_id = request.user.user_id
        
        # Get all current loans for the user
        user_loans = Loan.objects.filter(member_id=member_id, is_return=0)
        
        if not user_loans.exists():
            return Response(
                {'error': 'No active loans found for this user'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Create email content with all active loans
        loans_info = []
        for loan in user_loans:
            biblio_info = self.get_loan_biblio_info(loan)
            loans_info.append({
                'loan_id': loan.loan_id,
                'item_code': loan.item_code,
                'title': biblio_info['title'] if biblio_info else 'N/A',
                'loan_date': loan.loan_date,
                'due_date': loan.due_date
            })
        
        # Create email content
        email_subject = f"Loan Extension Request from Member {member_id}"
        
        # Format loans information for email
        loans_text = ""
        for loan_info in loans_info:
            loans_text += f"""Loan ID: {loan_info['loan_id']}
Item Code: {loan_info['item_code'] or 'N/A'}
Title: {loan_info['title']}
Loan Date: {loan_info['loan_date']}
Due Date: {loan_info['due_date']}

"""
        
        email_body = f"""Dear Admin,

A user has requested a loan extension for the following items:

Member ID: {member_id}

Book Information(s):
{loans_text}The user has provided the following WhatsApp number for contact:
{whatsapp_number}

Please process this extension request accordingly.

Best regards,
Library System
"""
        
        # Send email to admin
        try:
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@library.com',
                recipient_list=[settings.EMAIL_HOST_USER] if hasattr(settings, 'EMAIL_HOST_USER') else ['admin@library.com'],
                fail_silently=False,
            )
        except Exception as e:
            return Response(
                {'error': f'Failed to send email notification: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Return success response
        return Response(
            {'message': 'Loan extension request submitted successfully. Admin will be notified via email with all active loans and WhatsApp number.'},
            status=status.HTTP_200_OK
        )
    
    def is_valid_whatsapp_number(self, number):
        """Validate WhatsApp number format"""
        # Simple validation: should be numeric and have reasonable length
        # Should start with country code like 62 for Indonesia
        pattern = re.compile(r'^[1-9][0-9]{6,14}$')
        return bool(pattern.match(str(number).strip()))
    
    def get_loan_biblio_info(self, loan):
        """Get bibliographic information for a loan"""
        try:
            from .models import Item, Biblio
            if loan.item_code:
                item = Item.objects.get(item_code=loan.item_code)
                if item.biblio_id:
                    biblio = Biblio.objects.get(biblio_id=item.biblio_id)
                    return {
                        'title': biblio.title,
                        'isbn_issn': biblio.isbn_issn,
                        'call_number': biblio.call_number
                    }
        except (Item.DoesNotExist, Biblio.DoesNotExist):
            pass
        return None