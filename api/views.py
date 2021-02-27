from re import A
from bson.objectid import ObjectId
from django import http
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views import View
from pymongo import *
from rest_framework.response import Response
from rest_framework_jwt.serializers import User
from api.models import *
import api.response as res
from datetime import datetime
import re
from rest_framework.authtoken.models import Token
class advisorView(View):

    def get(self,request):
        return render(request,'advisor.html')
    def post(self,request):
        advisorname = request.POST.get('name')
        advisor_url = request.POST.get('photourl')
        if len(advisorname)<1 or len(advisor_url)<1:
            return HttpResponse(json.dumps(res.errors[400]))
        else:
            ad=Advisor(advisorname,advisor_url)
            ad.insertaobject(ad.todict(),ad.coll)
            return HttpResponse(json.dumps(res.success[200]))
    
class userregisterView(View):
    def get(self,request):
        return render(request,'user.html')

    def post(self,request):
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(username)<1 or len(email)<1 or len(password)<1:
            return  HttpResponse(json.dumps(res.errors[400]))
        else:
            ad=user(username,email,password)
            id = ad.insertaobject(ad.todict(),ad.coll)
            token,c=Token.objects.get_or_create()
            return HttpResponse(json.dumps({"jwt":token.key,
            "user_id":str(id),
            "status":res.success[200]}))

    
class userloginView(View):

    def get(self,request):
        return render(request,'userlogin.html')
        
    def post(self,request):

        email = request.POST.get('Username')
        password = request.POST.get('Password')
        if len(email)<1 or len(password)<1:
            return HttpResponse(json.dumps(res.errors[400]))
        else:
            ad=user('',email,password)
            resp= ad.getaobject({"email":email,"password":password},ad.coll)
            if type(resp) ==dict:
                token,c= Token.objects.get_or_create()
                return HttpResponse(json.dumps({"jwt":token.key,"user_id":str(resp["_id"]),"status":res.success[200]}))
                # return ObtainJSONWebToken()
            else:
                return HttpResponse(json.dumps(res.errors[401]))

def listalladvisor(request,id):
    us = user('','','')
    if us.userispresent(id):
        ad =Advisor('','')
        list_of_Advisor = ad.listalladvisor()
        return HttpResponse(json.dumps({"advisers":list_of_Advisor,"status":res.success[200]}))
    else:
        return HttpResponse(json.dumps({"error":"user is not present"}))

def bookacall(request,id,aid):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    b = booking(aid,id,dt_string)
    b.insertaobject(b.todict(),b.coll)
    return HttpResponse(json.dumps(res.success[200]))
# Create your views here.
def home(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    contents = body['content']
    return HttpResponse(contents)
