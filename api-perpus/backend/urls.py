from django.urls import path, include
from api.views.auth_views import register, login


urlpatterns = [
    path('api/', include('api.urls')),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]