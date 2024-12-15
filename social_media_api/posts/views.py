"""
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
#"""