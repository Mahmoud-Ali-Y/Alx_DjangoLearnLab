from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Post
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('blog/login.html', admin.site.urls),
    path('blog/logout.html'),
    path('blog/register.html'),
    path('blog/profile.html'),
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', SignUpView.as_view(next_page='login'),name='register'),
]