from django.db import models
from django.contrib.auth.models import User # 引入 Django 原生 User

class Member(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default="")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    joined_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username