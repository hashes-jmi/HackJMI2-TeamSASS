

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.deletion import CASCADE


# Create your models here.


class base_user(AbstractUser):
    def __str__(self):
        return f"username {self.username}"
class person(models.Model):
    title="user"
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=CASCADE,unique=True)
    name=models.CharField(max_length=20,blank=False)
    phone=models.PositiveIntegerField(blank=False)
    is_verified=models.BooleanField(default=False)
    num_of_otp=models.PositiveIntegerField(default=0)
    email=models.EmailField(blank=False)
class Hospital(models.Model):
    title="hospital"
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=CASCADE,unique=True)
    name=models.CharField(max_length=100,blank=False)