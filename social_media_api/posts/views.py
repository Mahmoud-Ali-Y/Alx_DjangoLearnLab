#"""
from django.shortcuts import render
from rest_framework.response import Response
#from knox.models import AuthToken
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import PostSerializer, CommentSerializer
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.messages import Message
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
"""
# Create your views here.
"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class FeedView():
    permissions_class = ['permissions.IsAuthenticated']
    def get_posts(self):
     following_users = Post.following.all()
     posts = Post.objects.filter(author__in=following_users).order_by(Post.created_at)

class LikeView():
    permissions_class = ['permissions.IsAuthenticated']
    def like_posts(self):
     return Response
    
class UnLikeView():
    permissions_class = ['permissions.IsAuthenticated']
    def unlike_posts(self):
     return Response

class NotificationView():
    permissions_class = ['permissions.IsAuthenticated']
    def send_notification(self):
     return Response

#"""