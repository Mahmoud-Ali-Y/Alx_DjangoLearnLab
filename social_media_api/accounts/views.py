#"""
from django.shortcuts import render
from rest_framework.response import Response
#from knox.models import AuthToken
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import CustomRegisterSerializer
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
class UserRegistration(CreateView):
    serializer_class = CustomRegisterSerializer
    template_name = "accounts/register.html"

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    authentication_classes = (TokenAuthentication)
    template_name = "accounts/login.html"
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        Message.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
class UserProfile(View):
    user = CustomUser.objects.all()
    def profile_page(request, username):
     user = get_object_or_404(CustomUser, username=username)
     return render(request, 'accounts/profile.html', {'profile_user': user})

class FollowingView(generics.GenericAPIView):
    permissions_class = ['permissions.IsAuthenticated']
    def follow_user():
        return Response
    def unfollow_user():
        return Response

#"""