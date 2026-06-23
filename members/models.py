from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from datetime import date
class Member(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, default="")
    joined_date = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        # 如果不是已經加密過的密碼，就加密
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username