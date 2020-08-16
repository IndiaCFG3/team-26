from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE , default=1)
    role = models.CharField(max_length=100)

class Form(models.Model):
    name = models.CharField(max_length=100)
    form_link = models.ManyToManyField(User)


class Question(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    form_link = models.ForeignKey(Form,on_delete=models.CASCADE,related_name='question',null=True,blank=True)
    
class Option(models.Model):
    name = models.CharField(max_length=100)
    question_link = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answer',null=True,blank=True)
