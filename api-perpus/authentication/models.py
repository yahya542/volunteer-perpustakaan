from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    nik = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Login(models.Model):
    password = models.CharField(max_length=100)
    nik = models.CharField(max_length=100)

    def __str__(self):
        return self.password
