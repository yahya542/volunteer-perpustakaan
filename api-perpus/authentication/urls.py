from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/', views.VerifyTokenView.as_view(), name='verify'),
    path('login/', views.LoginView.as_view(), name='login'),
]