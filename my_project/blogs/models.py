from django.db import models
from datetime import date
from django.utils import timezone



class Blog_User(models.Model):
    username= models.CharField('User name',
                               max_length=60
                               ,null=False)
    email=models.CharField('User email',
                           max_length=100)
    password=models.CharField('password',
                              max_length=100)


class Blog(models.Model):

    user_id=models.ForeignKey(Blog_User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    tittle=models.CharField("post tittle",max_length=200)
    post=models.TextField("Post")
    post_date=models.DateTimeField(default=timezone.now)
    good_name=models.CharField("Good name",max_length=50)


class Comment(models.Model):
    user_id = models.ForeignKey(Blog_User,on_delete=models.CASCADE)
    post_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    cmnt_date = models.DateTimeField(default=timezone.now)
    #name=models.CharField(default=Blog_User.username,max_length=60)
    comments=models.TextField("coment")


# Create your models here.
