from django.db import models



class User(models.Model):
    name=models.CharField('user name',max_length=60)
    fname=models.CharField('father name',max_length=60)
    email=models.TextField('email adress')
    age=models.IntegerField('age')

# Create your models here.
