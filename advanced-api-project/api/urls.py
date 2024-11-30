from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Book
from .views import CustomBookCreateView, CustomBookListView

router = DefaultRouter()
router.register(r'Book', CustomBookCreateView)
router.register(r'Book', CustomBookListView)

urlpatterns = [
    path('api/', include(router.urls)),
]