from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserViewSet, UserGroupViewSet, GroupAccessViewSet, SystemLogViewSet, RegisterView, LoginView, VerifyTokenView, RefreshTokenView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-groups', UserGroupViewSet)
router.register(r'group-access', GroupAccessViewSet)
router.register(r'system-logs', SystemLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Authentication endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'),
    # JWT Token endpoints
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]