from django.contrib import admin
from .models import *


class UserDetail(admin.ModelAdmin):
    list_display = ['name','fname','email','age']
admin.site.register(User,UserDetail)


# Register your models here.
