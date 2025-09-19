from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    realname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=64)
    fa = models.TextField(blank=True, null=True)  # 2fa renamed to fa
    email = models.CharField(max_length=200, blank=True, null=True)
    user_type = models.SmallIntegerField(blank=True, null=True)
    user_image = models.CharField(max_length=250, blank=True, null=True)
    social_media = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=15, blank=True, null=True)
    groups = models.CharField(max_length=200, blank=True, null=True)
    forgot = models.CharField(max_length=80, blank=True, null=True)
    admin_template = models.TextField(blank=True, null=True)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username

class UserGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30, unique=True)
    input_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'user_group'

    def __str__(self):
        return self.group_name

class GroupAccess(models.Model):
    group_id = models.IntegerField()
    module_id = models.IntegerField()
    menus = models.JSONField(blank=True, null=True)
    r = models.IntegerField(default=0)
    w = models.IntegerField(default=0)

    class Meta:
        db_table = 'group_access'
        unique_together = ('group_id', 'module_id')

    def __str__(self):
        return f"Group {self.group_id} - Module {self.module_id}"

class SystemLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_type = models.CharField(max_length=20, choices=[
        ('staff', 'Staff'),
        ('member', 'Member'),
        ('system', 'System')
    ], default='staff')
    id = models.CharField(max_length=50, blank=True, null=True)
    log_location = models.CharField(max_length=50)
    sub_module = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    log_msg = models.TextField()
    log_date = models.DateTimeField()

    class Meta:
        db_table = 'system_log'
        indexes = [
            models.Index(fields=['log_type']),
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return f"{self.log_type} - {self.log_location}"

class EmailVerification(models.Model):
    verification_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    token = models.CharField(max_length=100, unique=True)
    member_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    class Meta:
        db_table = 'email_verification'

    def __str__(self):
        return f"Verification for {self.email}"

    def is_expired(self):
        from django.utils import timezone
        return timezone.now() > self.expires_at
