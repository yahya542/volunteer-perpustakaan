from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BiblioViewSet, LoanHistoryViewSet, PublisherViewSet, AuthorViewSet
)

router = DefaultRouter()
# Main entities yang dibutuhkan
router.register(r'biblio', BiblioViewSet)
router.register(r'loan-history', LoanHistoryViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]