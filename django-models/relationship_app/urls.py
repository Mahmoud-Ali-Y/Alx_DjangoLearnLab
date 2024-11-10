from django.contrib import admin
from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Book/', Views.list_books, name = 'books')
    path('Library', Views.LibraryDetailView.as_Library(), name = 'Library')
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login')
    path('logout/', LogoutView.as_view(), name='logout')
    path('views.register/', LogoutView.as_view(template_name='relationship_app/register.html'))
    path('add_book/')
    path('edit_book/')
    path('delete_book/')
]