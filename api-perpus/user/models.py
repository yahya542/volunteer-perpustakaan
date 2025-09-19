from django.db import models
from rest_framework import serializers

class Member(models.Model):
    GENDER_CHOICES = [
        (0, 'Unknown'),
        (1, 'Male'),
        (2, 'Female'),
    ]

    member_id = models.CharField(max_length=20, primary_key=True)
    member_name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True, null=True)  # Added for tempat_lahir
    member_type_id = models.IntegerField(blank=True, null=True)
    member_address = models.CharField(max_length=255, blank=True, null=True)
    member_mail_address = models.CharField(max_length=255, blank=True, null=True)
    member_email = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    inst_name = models.CharField(max_length=100, blank=True, null=True)
    is_new = models.IntegerField(blank=True, null=True)
    member_image = models.CharField(max_length=200, blank=True, null=True)
    ktp_image = models.CharField(max_length=200, blank=True, null=True)  # Added for foto_ktp
    pin = models.CharField(max_length=50, blank=True, null=True)
    member_phone = models.CharField(max_length=50, blank=True, null=True)
    member_fax = models.CharField(max_length=50, blank=True, null=True)
    member_since_date = models.DateField(blank=True, null=True)
    register_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField()
    member_notes = models.TextField(blank=True, null=True)
    is_pending = models.SmallIntegerField(default=0)
    mpasswd = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=20, blank=True, null=True)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'
        indexes = [
            models.Index(fields=['member_name']),
            models.Index(fields=['member_type_id']),
        ]

    def __str__(self):
        return self.member_name

class MstMemberType(models.Model):
    member_type_id = models.AutoField(primary_key=True)
    member_type_name = models.CharField(max_length=50, unique=True)
    loan_limit = models.IntegerField()
    loan_periode = models.IntegerField()
    enable_reserve = models.IntegerField(default=0)
    reserve_limit = models.IntegerField(default=0)
    member_periode = models.IntegerField()
    reborrow_limit = models.IntegerField()
    fine_each_day = models.IntegerField()
    grace_periode = models.SmallIntegerField(default=0)
    input_date = models.DateField()
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mst_member_type'

    def __str__(self):
        return self.member_type_name

class VisitorCount(models.Model):
    visitor_id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20, blank=True, null=True)
    member_name = models.CharField(max_length=255)
    institution = models.CharField(max_length=100, blank=True, null=True)
    checkin_date = models.DateTimeField()

    class Meta:
        db_table = 'visitor_count'
        indexes = [
            models.Index(fields=['member_id']),
        ]

    def __str__(self):
        return f"{self.member_name} - {self.checkin_date}"

class MemberCustom(models.Model):
    member_id = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'member_custom'

    def __str__(self):
        return self.member_id

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    biblio_id = models.IntegerField()
    member_id = models.CharField(max_length=20)
    comment = models.TextField()
    input_date = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'

    def __str__(self):
        return f"Comment by {self.member_id} on {self.biblio_id}"

