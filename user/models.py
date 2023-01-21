import email
from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    username=models.CharField(max_length=10)
    Name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=200, null=True)
    Bio=models.TextField(blank=True,null=True)
    auth_image=models.ImageField(null=True,blank=True,upload_to='static/blogging/authors',default='ppp.jpg')
    instagram=models.CharField(max_length=200 , null=True)
    linkedin=models.CharField(max_length=200 , null=True)
    sign_up=models.DateTimeField(auto_now_add=True)
    twitter=models.CharField(max_length=200 , null=True)
    github=models.CharField(max_length=200 , null=True)
    
    
    class Meta:
        ordering=['sign_up']

    def __str__(self):
        return self.user.username    

