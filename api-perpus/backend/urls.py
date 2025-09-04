from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from authentication.views import register, login


urlpatterns = [
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # OpenAPI schema endpoint
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI for API documentation


]