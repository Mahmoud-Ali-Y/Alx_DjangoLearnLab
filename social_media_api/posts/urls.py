from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import *
from .views import *
from django.contrib.auth.views import LogoutView

#"""
router = DefaultRouter()
router.register(r'Post', PostViewSet)
router.register(r'Comment', CommentViewSet)

urlpatterns = [
    path('posts/', include(router.urls)),
    ]
#"""