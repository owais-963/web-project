from rest_framework import serializers
from .models import User
"""
class Userserializer(serializers.Serializer):
    name=serializers.CharField(max_length=60)
    fname=serializers.CharField(max_length=60)
    email=serializers.CharField(max_length=None,allow_blank=False,trim_whitespace=True)
    age=serializers.IntegerField()
    adress=models.CharField(max_length=None,allow_blank=False,trim_whitespace=True)
    education=models.CharField(max_length=20)
    school=models.CharField(max_length=100)"""


class Userserializer(serializers.Serializer):
    name=serializers.CharField(max_length=60)
    fname=serializers.CharField(max_length=60)
    email=serializers.EmailField()
    age=serializers.IntegerField()


def create(self,validated_data):
    return User.objects.create(**validated_data)