#"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.models import *
from posts.views import PostViewSet, CommentViewSet, FeedView, LikeView, UnLikeView, NotificationView
from django.contrib.auth.views import LogoutView
"""
"""
router = DefaultRouter()
router.register(r'Post', PostViewSet)
router.register(r'Comment', CommentViewSet)

urlpatterns = [
    path('posts/', include(router.urls)),
    path('feed/', FeedView.as_view(),name='login'),
    path('/posts/<int:pk>/like/', LikeView.as_view(),name='login'),
    path('/posts/<int:pk>/unlike/', UnLikeView.as_view(),name='login'),
    path('/notifications/', NotificationView.as_view(),name='login'),
    ]
#"""