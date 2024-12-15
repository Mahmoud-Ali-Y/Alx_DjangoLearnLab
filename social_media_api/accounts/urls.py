#"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.models import *
from accounts.views import UserProfile, UserRegistration, UserLoginView, FollowingView , UnFollowingView
from django.contrib.auth.views import LogoutView
"""
"""


urlpatterns = [
    path('blog/login/', UserLoginView.as_view(),name='login'),
    path('blog/logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('blog/register/', UserRegistration.as_view(next_page='login'),name='register'),
    path('blog/profile/', UserProfile.as_view(),name='profile'),
    path('unfollow/<int:user_id>/', FollowingView.as_view(),name='profile'),
    path('follow/<int:user_id>', UnFollowingView.as_view(),name='profile'),
    ]
#"""