from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import *
from .views import *
from django.contrib.auth.views import LogoutView

#"""
urlpatterns = [
    path('blog/login/', UserLoginView.as_view(),name='login'),
    path('blog/logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('blog/register/', UserRegistration.as_view(next_page='login'),name='register'),
    path('blog/profile/', UserProfile.as_view(),name='profile'),
    ]
#"""