from django.db import models
from authentication.models import Login

class Profile(models.Model):
    GENDER_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    
    MEMBERSHIP_CHOICES = [
        ('REGULAR', 'Regular'),
        ('PREMIUM', 'Premium'),
        ('VIP', 'VIP'),
    ]
    
    login = models.OneToOneField(Login, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    nik = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    tempat_lahir = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    institusi = models.CharField(max_length=200, blank=True, null=True)
    keanggotaan = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES, default='REGULAR')
    jenis_kelamin = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    foto_diri = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    foto_ktp = models.ImageField(upload_to='ktp_photos/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
