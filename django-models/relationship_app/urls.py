from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Book/', Views.books, name = 'books')
    path('Library', Views.Library_books.as_Library(), name = 'Library')
]