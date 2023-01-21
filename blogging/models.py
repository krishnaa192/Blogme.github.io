from distutils.command.upload import upload
from operator import truediv
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
import uuid
from user.models import Profile
from ckeditor.fields import RichTextField




class Tags(models.Model):
    name=models.CharField(max_length=9)
    created=models.DateTimeField(auto_now_add=TRUE)
    id=models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
   
    class Meta:
        ordering=['created']

    def __str__(self):
        return self.name 


class Blog(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,unique=False)
    Author=models.ForeignKey(Profile,on_delete=models.CASCADE,name="Author", null="True")
    blog=RichTextField()
    blog_title=models.CharField(max_length=33)
    desc=models.CharField(max_length=100, null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    blog_image = models.ImageField(
        null=True, blank=True, default="ppp.jpg")
    Pen_name=models.CharField(max_length=7)
    tags=models.ForeignKey(Tags, on_delete=models.CASCADE,null=True,blank=True,name="tags")
    upload=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['upload']

    def __str__(self):
        return self.blog_title    