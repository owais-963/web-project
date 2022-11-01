from django.contrib import admin
from .models import *


class  User_Detail(admin.ModelAdmin):
    list_display = ['username','email']


class Blog_Detail(admin.ModelAdmin):
    list_display = ['good_name','tittle','post_date']


admin.site.register(Blog,Blog_Detail)
admin.site.register(Blog_User,User_Detail)
admin.site.register(Comment)
# Register your models here.
