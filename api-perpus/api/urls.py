from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BiblioViewSet, LoanHistoryViewSet
)

router = DefaultRouter()
# Main entities yang dibutuhkan
router.register(r'biblio', BiblioViewSet)
router.register(r'loan-history', LoanHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
