from django.contrib import admin
from django.urls import path
from . import views

# app_name='blogging'

urlpatterns = [
    path("", views.Home, name="Home"),
    path('authors/', views.authors, name="authors"),
    path('Blogpage/', views.Blogpage, name="Blogpage"),
    path('Read/<str:pk>/', views.Read, name="Read"),
    path('Submit_Form',views.Submit_Form,name="Submit_Form"),
    path('update_blog/<str:pk>/', views.update_blog, name="update_blog"),
    path('delete_blog/<str:pk>/', views.delete_blog, name="delete_blog"),
    path('all_blog/', views.all_blog,name="all_blog"),

]

