from django.contrib.auth.models import User
from django.db.models import base
from django.shortcuts import render,HttpResponse
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from sendgrid.helpers import mail
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
from .serializers import *
from mailjet_rest import Client
from .utils import render_to_pdf
# Create your views here.

class Register(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data['name'])
        name=request.data['name']
        phone_num=request.data['phone']
        email=request.data['email']
        aadhar=request.data['aadhar']
        user_address=address.objects.create(country=request.data['address']['country'],state=request.data['address']['state'],pincode=request.data['address']['pincode'],address_line1=request.data['address']['line1'])

        try:
            user_base=base_user.objects.create(username=uuid.uuid4())
            user_base.save()
            user_address.save()
            new_person=person.objects.create(user=user_base,name=name,phone=phone_num,email=email,aadhar=aadhar,user_address=user_address)
            new_person.save()
            return Response({"status":"verify please","E-id":user_base.username})
        except:
            return Response("Invalid Input")
    
class RegistrationHospital(APIView):
    def post(self,request,*args,**kwargs):
        name=request.data['name']
        email=request.data['email']
        # password=request.data['password']
        hospital_address=address.objects.create(country=request.data['address']['country'],state=request.data['address']['state'],pincode=request.data['address']['pincode'],address_line1=request.data['address']['line1'])
        try:
            hospital_base=base_user.objects.create(username=uuid.uuid4())
            hospital_base.save()
            hospital_address.save()
            new_hospital=Hospital.objects.create(user=hospital_base,name=name,email=email,hospital_address=hospital_address)
            new_hospital.save()
            return Response({'status':'Verify Please','E-id':hospital_base.username})
        except:
            return Response("invalid input")

class GenerateOTP_Hospital(APIView):
    def post(self,request,*args,**kwargs):
        eid=request.data['eid']
        getHospital=base_user.objects.get(username=eid)
        hospital_inst=Hospital.objects.get(user=getHospital)
    
        hospital_inst.num_of_otp+=1
        hospital_inst.save()
        otp=generateOTP(hospital_inst.email,hospital_inst.num_of_otp)
        api_key = 'adf2c704fc5bbc9f699f6c5ecc8a26b4'
        api_secret = '3910da862badeabf44145829e1c1364a'
        mailjet=Client(auth=(api_key,api_secret),version='v3.1')
        data={
            'Messages':[{
                "From":{
                    "Email":"gamma110005@gmail.com",
                    "Name":"HealthID"
                },
                "To":[
                    {
                        "Email":hospital_inst.email,
                        "Name":"Testing"
                    }
                ]
            ,
            "Subject":"OTP Verification",
            "TextPart":f"OTP verification is {otp}",
            "HTMLPart":f"<h2>OTP Verification is {otp}",
            "CustomID":"AppGettingStartedTest"
            }
            ]
        }

        print(otp)
        try:
            # sg=SendGridAPIClient('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')
            # message=Mail(
            #     from_email="mhodsaif.sps@gmail.com",
            #     to_emails=personUser.email,
            #     subject='OTP verification',
            #     html_content=f'<h1>Your otp is {otp}</h1>'
            # )
            response=mailjet.send.create(data=data)
            print(response.status_code)
            
            print(response.json())
            if(response.status_code==200):
                return Response({'status':'otp send successfully','otp':otp})
            else:
                return Response("Error Occured")
        except Exception as e:
            print(e)
            return Response({'error occured'})

class GetStatsBMI(APIView):
    def post(self,request,*args,**kwargs):
        BMIList=[]
        if "pincode" in request.data:
            pincode=request.data["pincode"]

            person_list=person.objects.filter(user_address__in=address.objects.filter(pincode=pincode))
            print(person_list)
            

            for person_each in person_list:
                    BMIList+=[person_each.basic_medical_data.BMI]
            print(BMIList)
            return Response(BMIList)
        elif "state" in request.data:
            state=request.data['state']
            person_list=person.objects.filter(user_address__in=address.objects.filter(state=state))
            print(person_list)
            for person_each in person_list:
                    BMIList+=[person_each.basic_medical_data.BMI]
            print(BMIList)
            return Response(BMIList)
class VerifyOTP_Hospital(APIView):
    def post(self,request,*args,**kwargs):
        otp=request.data['otp']
        eid=request.data['eid']
        getHospital_base=base_user.objects.get(username=eid)
        hospital_inst=Hospital.objects.get(user=getHospital_base)        
        if verifyOTP(hospital_inst.email,hospital_inst.num_of_otp,otp):
            hospital_inst.is_verified=True
            hospital_inst.save()
            refresh=RefreshToken.for_user(getHospital_base)
        
            return Response({'status':"Success",'access':str(refresh.access_token)})
        return Response("OTP is wrong",status=401)


class ViewEID_Details(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        userBase=request.user
        
        try:
            hospital_inst=Hospital.objects.get(user=userBase)
            if hospital_inst.is_verified==True:
                eid=request.data['eid']
                otherUserbase=base_user.objects.get(username=eid)
                personInst=person.objects.get(user=otherUserbase)
                data=GetUserInfo_Personal(personInst).data
                return Response(data)
            else:
                return Response("Not verified",status=401)
        except Exception as e:
            print(e)
            return Response("Not Authorized",status=401)
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
class GetPersonData(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        person_data=person.objects.get(user=request.user)
        if person_data.is_verified==True:
            data=GetUserInfo_Personal(person_data).data
            return Response(data)
        else:
            return Response({"status":"Not verified"})
class GenerateOTP(APIView):
    permission_classes=[AllowAny]
    def post(self,request,*args,**kwargs):
        aadhar=request.data['aadhar']
       
        personUser=person.objects.get(aadhar=aadhar)
        getuser=personUser.user
        personUser.num_of_otp+=1
        personUser.save()
        otp=generateOTP(personUser.email,personUser.num_of_otp)
        api_key = 'adf2c704fc5bbc9f699f6c5ecc8a26b4'
        api_secret = '3910da862badeabf44145829e1c1364a'
        mailjet=Client(auth=(api_key,api_secret),version='v3.1')
        data={
            'Messages':[{
                "From":{
                    "Email":"gamma110005@gmail.com",
                    "Name":"HealthID"
                },
                "To":[
                    {
                        "Email":personUser.email,
                        "Name":"Testing"
                    }
                ]
            ,
            "Subject":"OTP Verification",
            "TextPart":f"OTP verification is {otp}",
            "HTMLPart":f"<h2>OTP Verification is {otp}",
            "CustomID":"AppGettingStartedTest"
            }
            ]
        }

        print(otp)
        try:
            # sg=SendGridAPIClient('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')
            # message=Mail(
            #     from_email="mhodsaif.sps@gmail.com",
            #     to_emails=personUser.email,
            #     subject='OTP verification',
            #     html_content=f'<h1>Your otp is {otp}</h1>'
            # )
            response=mailjet.send.create(data=data)
            print(response.status_code)
            
            print(response.json())
            if(response.status_code==200):
                return Response({'status':'otp send successfully','otp':otp})
            else:
                return Response("Error Occured")
        except Exception as e:
            print(e)
            return Response({'error occured'})

class VerifyOTP(APIView):
    def post(self,request,*args,**kwargs):
        otp=request.data['otp']
        aadhar=request.data['aadhar']
        personUser=person.objects.get(aadhar=aadhar)
        getuser=personUser.user
        if verifyOTP(personUser.email,personUser.num_of_otp,otp):
            personUser.is_verified=True
            personUser.save()
            refresh=RefreshToken.for_user(getuser)
        
            return Response({'status':"Success",'access':str(refresh.access_token)})
        return Response("OTP is wrong")


class AddMedicalData(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        personData=person.objects.get(user=request.user)

        if personData.is_verified==True:
            if personData.basic_medical_data=='':
                basic_medical_info=basic_medical.objects.create()
                basic_medical_info.save()
                personData.basic_medical_data=basic_medical_info
                personData.save()
            if "basic_info" in request.data:
                
                if "height" in request.data['basic_info']:
                    personData.basic_medical_data.height=request.data['basic_info']['height']
                if "weight" in request.data['basic_info']:
                    personData.basic_medical_data.weight=request.data['basic_info']['weight']
                if "blood_group" in request.data['basic_info']:
                    personData.basic_medical_data.blood_group=request.data['basic_info']['blood_group']
                
                personData.basic_medical_data.save()
        
        return Response("workin")        

class GetLocationInfo(APIView):
    # permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        # userBase=request.user
        # personData=person.objects.get(user=userBase)
        pincode=request.data['pincode']
        address_list=person.objects.filter(user_address__in=address.objects.filter(pincode=pincode))

        disease_list=basic_medical.objects.filter(disease__in=Disease.objects.filter(is_communicatable=True),basic_medical_of__in=address_list)
        d=Disease.objects.filter(is_communicatable=True,belong__in=disease_list,is_current=True)        
        print(d)
        return Response(d.count())
        
class GeneratePdf(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        personData=person.objects.get(pk=1)
        context=GetUserInfo_Personal(personData).data
        print(context)
        pdf=render_to_pdf('Ecard.html',context)
       
        return HttpResponse(pdf,content_type='application/pdf')

class OrgRegister(APIView):
    def post(self,request,*args,**kwargs):
        name=request.data['name']
        # phone_num=request.data['phone']
        email=request.data['email']
        # aadhar=request.data['aadhar']
        org_address=address.objects.create(country=request.data['address']['country'],state=request.data['address']['state'],pincode=request.data['address']['pincode'],address_line1=request.data['address']['line1'])

        try:
            org_base=base_user.objects.create(username=uuid.uuid4())
            org_base.save()
            org_address.save()
            new_org=organization.objects.create(user=org_base,name=name,email=email,organization_address=org_address)
            new_org.save()
            return Response({"status":"verify please","E-id":org_base.username})
        except:
            return Response("Invalid Input")
class OrgGenerateOTP(APIView):
    def post(self,request,*args,**kwargs):
        eid=request.data['eid']
        getOrg=base_user.objects.get(username=eid)
        org_inst=organization.objects.get(user=getOrg)
    
        org_inst.num_of_otp+=1
        org_inst.save()
        otp=generateOTP(org_inst.email,org_inst.num_of_otp)
        api_key = 'adf2c704fc5bbc9f699f6c5ecc8a26b4'
        api_secret = '3910da862badeabf44145829e1c1364a'
        mailjet=Client(auth=(api_key,api_secret),version='v3.1')
        data={
            'Messages':[{
                "From":{
                    "Email":"gamma110005@gmail.com",
                    "Name":"HealthID"
                },
                "To":[
                    {
                        "Email":org_inst.email,
                        "Name":org_inst.name+" verification"
                    }
                ]
            ,
            "Subject":"OTP Verification",
            "TextPart":f"OTP verification is {otp}",
            "HTMLPart":f"<h2>OTP Verification is {otp}",
            "CustomID":"AppGettingStartedTest"
            }
            ]
        }

        print(otp)
        try:
            # sg=SendGridAPIClient('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')
            # message=Mail(
            #     from_email="mhodsaif.sps@gmail.com",
            #     to_emails=personUser.email,
            #     subject='OTP verification',
            #     html_content=f'<h1>Your otp is {otp}</h1>'
            # )
            response=mailjet.send.create(data=data)
            print(response.status_code)
            
            print(response.json())
            if(response.status_code==200):
                return Response({'status':'otp send successfully','otp':otp})
            else:
                return Response("Error Occured")
        except Exception as e:
            print(e)
            return Response({'error occured'})
class VerifyOrgOTP(APIView):
    def post(self,request,*args,**kwargs):
        otp=request.data['otp']
        eid=request.data['eid']
        getorg=base_user.objects.get(username=eid)
        org_inst=organization.objects.get(user=getorg)
        
        if verifyOTP(org_inst.email,org_inst.num_of_otp,otp):
            org_inst.is_verified=True
            org_inst.save()
            refresh=RefreshToken.for_user(getorg)
        
            return Response({'status':"Success",'access':str(refresh.access_token)})
        return Response("OTP is wrong")
class Org_GetEID(APIView):
    def post(self,request,*args,**kwargs):
        try:
            orgInst=organization.objects.get(user=request.user)

            eid=request.data['eid']
            getperson=base_user.objects.get(username=eid)
            personInst=person.objects.get(user=getperson)
            personData=GetUserInfo_Personal(personInst).data
            return Response(personData)
        except:
             return Response("Organization not found")
        

class IndexInfo(APIView):
    def get(self,request,*args,**kwargs):
        personCount=person.objects.all().count()
        organizationCount=organization.objects.all().count()
        hospitalCount=Hospital.objects.all().count()


        return Response({
            "person":personCount,
            "org":organizationCount,
            "hospital":hospitalCount
        })
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