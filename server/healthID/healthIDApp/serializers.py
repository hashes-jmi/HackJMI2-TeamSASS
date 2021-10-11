from django.db.models import base, fields
from rest_framework import serializers
from .models import *




class GetE_ID(serializers.ModelSerializer):
    class Meta:
        model=base_user
        fields=['username']
class Get_Address(serializers.ModelSerializer):
    class Meta:
        model=address
        fields=['address_line1','state','pincode','country']
class Get_Allergies(serializers.ModelSerializer):
    class Meta:
        model=Allergies
        fields=['name']
class Get_Surgery(serializers.ModelSerializer):
    class Meta:
        model=Surgery
        fields=['name','date']
class Get_Disease(serializers.ModelSerializer):
    class Meta:
        model=Disease
        fields=['name','last_diagnose','is_current']
class Get_Basic_Medical(serializers.ModelSerializer):
    allergies=Get_Allergies(many=True)
    surgery=Get_Surgery(many=True)
    disease=Get_Disease(many=True)
    class Meta:
        model=basic_medical
        fields=['height','weight','blood_group','allergies','surgery','disease']
        # ,,'surgery','disease']
class GetUserInfo_Personal(serializers.ModelSerializer):
    user=GetE_ID()
    user_address=Get_Address()
    basic_medical_data=Get_Basic_Medical()
    class Meta:
        model=person
        fields=['name','user','is_verified','user_address','basic_medical_data']