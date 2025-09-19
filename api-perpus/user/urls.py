from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, MstMemberTypeViewSet, VisitorCountViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'member-types', MstMemberTypeViewSet)
router.register(r'visitors', VisitorCountViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]