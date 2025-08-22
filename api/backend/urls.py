from django.urls import path, include
from ..views.views import register


urlpatterns = [
    path('api/', include('api.urls')),
    path('register/', register, name='register'),
]