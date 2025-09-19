from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BiblioViewSet, ItemViewSet, LoanViewSet, ReserveViewSet, FinesViewSet, LoanHistoryViewSet,
    MstGmdViewSet, MstLanguageViewSet, MstLocationViewSet, MstCollTypeViewSet, MstItemStatusViewSet,
    MstPublisherViewSet, MstPlaceViewSet, MstSupplierViewSet, MstAuthorViewSet, MstTopicViewSet,
    MstFrequencyViewSet, MstLoanRulesViewSet, MstLabelViewSet, SettingViewSet
)

router = DefaultRouter()
# Main entities
router.register(r'biblio', BiblioViewSet)
router.register(r'items', ItemViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'reserves', ReserveViewSet)
router.register(r'fines', FinesViewSet)
router.register(r'loan-history', LoanHistoryViewSet)

# Master data
router.register(r'gmd', MstGmdViewSet)
router.register(r'languages', MstLanguageViewSet)
router.register(r'locations', MstLocationViewSet)
router.register(r'collection-types', MstCollTypeViewSet)
router.register(r'item-status', MstItemStatusViewSet)
router.register(r'publishers', MstPublisherViewSet)
router.register(r'places', MstPlaceViewSet)
router.register(r'suppliers', MstSupplierViewSet)
router.register(r'authors', MstAuthorViewSet)
router.register(r'topics', MstTopicViewSet)
router.register(r'frequencies', MstFrequencyViewSet)
router.register(r'loan-rules', MstLoanRulesViewSet)
router.register(r'labels', MstLabelViewSet)
router.register(r'settings', SettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
