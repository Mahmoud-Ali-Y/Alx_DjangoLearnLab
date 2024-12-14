from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Post
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('blog/login.html'),
    path('blog/logout.html'),
    path('blog/register.html'),
    path('blog/profile.html'),
    path('blog/login/', MyLoginView.as_view(),name='login'),
    path('blog/logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('blog/register/', UserCreationForm.as_view(next_page='login'),name='register'),
    path('blog/profile/'),
    path('/posts/', PostListView.as_view(), name='post'),
    path('/posts/<int:pk>/', PostDetailView.as_view(), name='details'),
    path('/post/new/', PostCreateView.as_view(), name='new'),
    path('/post/<int:pk>/update/', PostUpdateView.as_view(), name='edit'),
    path('/post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]