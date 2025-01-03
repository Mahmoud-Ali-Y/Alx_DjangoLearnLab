from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Book
from .views import *

router = DefaultRouter()
router.register(r'Book', CustomBookCreateView)
router.register(r'Book', CustomBookDetailView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/books', admin.site.urls),
    path('api/books/create'),
    path('api/books/update'),
    path('api/books/delete'),
]