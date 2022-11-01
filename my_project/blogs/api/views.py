from rest_framework import status
from rest_framework.response import responses
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from blogs.models import Blog
from blogs.api.serializers import BlogSerializer

def get_api_view(request,id):
    blog=Blog.objects.get(id=id)
    serializer=BlogSerializer(blog)
