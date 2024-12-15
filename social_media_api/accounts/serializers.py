from models import *
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
#"""
class CustomRegisterSerializer(RegisterSerializer):
    bio = serializers.CharField()
    profile_picture = serializers.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    token = Token.objects.create()

    def CreateUser():
        user = get_user_model().objects.create_user(username = None, email = None, password = None, bio = None, profile_picture = None)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
#"""