from models import *
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    bio = serializers.TextField()
    profile_picture = serializers.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')