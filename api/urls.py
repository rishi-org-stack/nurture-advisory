from django.contrib import admin
from django.urls import path
from api.views import *
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path("admin/advisor/",advisorView.as_view(),name="advisor"),
    path("user/register/",userregisterView.as_view(),name="resgister"),
    path("user/login/",userloginView.as_view(),name="login"),
    path("user/<id>/advisor/",listalladvisor,name= "listview"),
    path("user/<id>/advisor/<aid>",bookacall,name="bookin"),
    path("test/",obtain_jwt_token)
]