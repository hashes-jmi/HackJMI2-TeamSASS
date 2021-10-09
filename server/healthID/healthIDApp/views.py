from django.contrib.auth.models import User
from django.db.models import base
from django.shortcuts import render,HttpResponse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.db import IntegrityError
import uuid
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny
import base64
import pyotp
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Create your views here.

class Register(APIView):
    def get(self,request,*args,**kwargs):
        name=request.data['name']
        phone_num=request.data['phone']
        email=request.data['email']
        try:
            user_base=base_user.objects.create(username=uuid.uuid4())
            user_base.save()
            new_person=person.objects.create(user=user_base,name=name,phone=phone_num,email=email)
            new_person.save()
            return Response({"status":"verify please","E-id":user_base.username})
        except:
            return Response("Invalid Input")
    
# class login(APIView):
#     def get(self,request,*args,**kwargs):
        
#         eid=request.data['eid']
#         user_data=base_user.objects.get(username=eid)
#         personUser=person.objects.get(user=user_data)
#         personUser.num_of_otp+=1
#         personUser.save()
#         otp=generateOTP(personUser.email,personUser.num_of_otp)

#         if(request.data['otp']=="123"):
            
#             refresh=RefreshToken.for_user(base_user.objects.get(username=id))
#             return Response({'access':str(refresh.access_token)})
#         else:
#             return Response({'issue'})
class Working(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        person_data=person.objects.get(user=request.user)
        if person_data.is_verified==True:
            return Response("login working")
        else:
            return Response({"status":"Not verified"})
class GenerateOTP(APIView):
    permission_classes=[AllowAny]
    def get(self,request,*args,**kwargs):
        eid=request.data['eid']
        getuser=base_user.objects.get(username=eid)
        personUser=person.objects.get(user=getuser)
        personUser.num_of_otp+=1
        personUser.save()
        otp=generateOTP(personUser.email,personUser.num_of_otp)
        try:
            sg=SendGridAPIClient('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')
            message=Mail(
                from_email="mhodsaif.sps@gmail.com",
                to_emails=personUser.email,
                subject='OTP verification',
                html_content=f'<h1>Your otp is {otp}</h1>'
            )
            response=sg.send(message)
            if(response.status_code==202):
                return Response({'otp send successfully'})
        except Exception as e:
            print(e)
            return Response({'error occured'})

class VerifyOTP(APIView):
    def post(self,request,*argsm,**kwargs):
        otp=request.data['otp']
        eid=request.data['eid']
        getuser=base_user.objects.get(username=eid)
        personUser=person.objects.get(user=getuser)
        if verifyOTP(personUser.email,personUser.num_of_otp,otp):
            personUser.is_verified=True
            personUser.save()
            refresh=RefreshToken.for_user(getuser)
        
            return Response({'status':"Success",'access':str(refresh.access_token)})
        return Response("OTP is wrong")



def generateOTP(email,num_of_otp):
    keygen=str(email)+"RNijLmlGONx4qgGCrgvm"
    key=base64.b32encode(keygen.encode())
    otp=pyotp.HOTP(key)
    return otp.at(num_of_otp)

def verifyOTP(email,num_of_otp,otp):
    keygen=str(email)+"RNijLmlGONx4qgGCrgvm"
    key=base64.b32encode(keygen.encode())
    otpCheck=pyotp.HOTP(key)
    return otpCheck.verify(int(otp),num_of_otp)