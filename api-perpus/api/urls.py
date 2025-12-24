from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BiblioViewSet, PublisherViewSet, AuthorViewSet, MemberLoanHistoryView, CurrentLoansViewSet, LoanHistoryView, LoanExtensionRequestView
)

router = DefaultRouter()
# Main entities yang dibutuhkan
router.register(r'biblio', BiblioViewSet)
# LoanHistoryViewSet removed - now using path() for custom endpoint
router.register(r'loan', CurrentLoansViewSet, basename='loan')
router.register(r'publishers', PublisherViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Direct endpoint for member loan history
    path('loan-history/member/<str:member_id>/', MemberLoanHistoryView.as_view(), name='member-loan-history'),
    # Direct endpoint for current user's loan history
    path('loan-history/', LoanHistoryView.as_view(), name='loan-history'),
    # Direct endpoint for loan extension request
    path('loan/extension-request/', LoanExtensionRequestView.as_view(), name='loan-extension-request'),
]

