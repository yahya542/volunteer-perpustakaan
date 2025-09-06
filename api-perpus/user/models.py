from django.db import models
from authentication.models import Login

class Profile(models.Model):
    login = models.OneToOneField(Login, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    nik = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
