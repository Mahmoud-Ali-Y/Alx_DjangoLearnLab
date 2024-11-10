from django.contrib import admin
from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Book/', Views.list_books, name = 'books')
    path('pk', Views.LibraryDetailView.as_view(), name = 'Library')
]