from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import responses

def index(request):
    return HttpResponse("Welcome")
def user_detail(request,id):
    user=User.objects.get(id=id)
    serializer=Userserializer(user)
    #json_data=JSONRenderer().render(serializer.data)
    return JsonResponse(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')


#via Query set

def user_list(request):
    user=User.objects.all()
    serializer=Userserializer(user, many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
#
@csrf_exempt
def edit_user(request):
   if request.method=='POST':
       json_data=request.body
       stream=io.BytesIO(json_data)
       python_Data=JSONParser().parse(stream)
       serializer=Userserializer(data=python_Data)
       if serializer.is_valid():
           serializer.save()
           mesg={"msg":"Data Recived"}
           json_data=JSONRenderer().render(mesg)
           return HttpResponse(json_data,content_type='application/json')
       else:
           json_data=JSONRenderer().render(serializer.errors)
           return HttpResponse(json_data,content_type='application/json')
   else:
       return HttpResponse("run fine but no data recived")


