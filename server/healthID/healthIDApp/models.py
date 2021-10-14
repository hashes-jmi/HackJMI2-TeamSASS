

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.utils import tree


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
    aadhar=models.PositiveIntegerField(blank=True)
    user_address=models.OneToOneField('address',on_delete=CASCADE,null=True,related_name="address_of")
    basic_medical_data=models.OneToOneField('basic_medical',on_delete=DO_NOTHING,blank=True,null=True,related_name="basic_medical_of")
class address(models.Model):
    country=models.CharField(max_length=15)
    state=models.CharField(max_length=30)
    pincode=models.PositiveIntegerField()
    address_line1=models.TextField()

class basic_medical(models.Model):
    height=models.PositiveSmallIntegerField(null=True)
    weight=models.PositiveSmallIntegerField(null=True)
    blood_group=models.TextField(null=True)
class Hospital(models.Model):
    title="hospital"
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=CASCADE,unique=True)
    name=models.CharField(max_length=100,blank=False)
    hospital_address=models.OneToOneField('address',on_delete=CASCADE,null=True)
    email=models.EmailField(blank=True)
    num_of_otp=models.PositiveIntegerField(default=0)
    is_verified=models.BooleanField(default=False)
class Allergies(models.Model):
    name=models.CharField(max_length=10)
    belong=models.ForeignKey(basic_medical,on_delete=CASCADE,related_name="allergies",null=True)

class Surgery(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField()
    belong=models.ForeignKey(basic_medical,on_delete=CASCADE,related_name="surgery",null=True)

class Disease(models.Model):
    name=models.CharField(max_length=20)
    last_diagnose=models.DateField()
    is_current=models.BooleanField()
    belong=models.ForeignKey(basic_medical,on_delete=CASCADE,related_name="disease",null=True)
    is_communicatable=models.BooleanField()

    def __str__(self):
        return f"name :{self.name}"
