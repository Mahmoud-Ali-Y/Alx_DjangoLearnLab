from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from .models import Library
# Create your views here.
def books(request):
  books = Book.objects.all().values()
  template = loader.get_template('relationship_app/list_books.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))
 # return HttpResponse(context, request)

class Library_books(Library):
 def get(self, request):
  self.library_name = pass
  self.library = Library.objects.get(name=self.library_name)
  self.library_books = Book.objects.filter(id = self.library.books)
  template = loader.get_template('relationship_app/library_detail.html')
  context = {
    'books': self.library_books,
  }
  return HttpResponse(template.render(context, request))