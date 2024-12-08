from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Post
from .views import *

urlpatterns = [
    path('blog/login.html', admin.site.urls),
    path('blog/logout.html'),
    path('blog/registration.html'),
    path('blog/profile.html'),
]