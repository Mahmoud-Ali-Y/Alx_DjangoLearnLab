from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractBaseUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    followers = models.ManyToManyField('self', symmetrical=False)