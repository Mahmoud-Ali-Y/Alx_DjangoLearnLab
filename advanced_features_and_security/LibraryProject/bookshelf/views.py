from django.shortcuts import render
from .models import *
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.template import loader
from django.forms import ExampleForm
# Create your views here.
@permission_required('app_name.can_edit', raise_exception=True)
def book_list(request):
  books = Book.objects.all().values()
  template = loader.get_template('relationship_app/list_books.html')
  context = {
    'books': books,
  }
@permission_required('app_name.can_edit', raise_exception=True)
def books(request):
  books = Book.objects.all().values()
  template = loader.get_template('relationship_app/list_books.html')
  context = {
    'books': books,
  }