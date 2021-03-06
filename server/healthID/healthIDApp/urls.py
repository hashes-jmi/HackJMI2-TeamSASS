from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns=[

    path('register',Register.as_view()),
    path('login-otp',GenerateOTP.as_view()),
    path("user-info",GetPersonData.as_view()),
    path('user-info/add',AddMedicalData.as_view()),
    # path("generate-otp",GenerateOTP.as_view()),
    path("verify-otp",VerifyOTP.as_view()),
    path("hospital/register",RegistrationHospital.as_view()),
    path("hospital/login-otp",GenerateOTP_Hospital.as_view()),
    path("hospital/verify-otp",VerifyOTP_Hospital.as_view()),
    path("hospital/getInfo",ViewEID_Details.as_view()),
    path("user-info/getLocationStatus",GetLocationInfo.as_view()),
    path("card",GeneratePdf.as_view()),
    path("getStats",GetStatsBMI.as_view()),
    path("org/register",OrgRegister.as_view()),
    path("org/login",OrgGenerateOTP.as_view()),
    path("org/verify",VerifyOrgOTP.as_view()),
    path("org/getInfo",Org_GetEID.as_view()),
    path("indexInfo",IndexInfo.as_view())
    # path('/token',TokenObtainPairView.as_view(),name="obtain_token"),
    # path('/token/refresh',TokenRefreshView.as_view(),name="refresh_token"),path('/token/verify',TokenVerifyView.as_view(),name="verify_token")
]