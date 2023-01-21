from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.authors, name="authors"),
    path('login/', views.loginuser, name="login"),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutuser, name="logout"),
    path('edit_profile', views.edit_profile, name="edit_profile"),

    
]

 