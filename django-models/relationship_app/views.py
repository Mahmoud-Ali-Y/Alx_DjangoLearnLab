from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from .models import Library
from django.views.generic.detail import DetailView
# Create your views here.
def list_books(request):
  books = Book.objects.all().values()
  template = loader.get_template('relationship_app/list_books.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))
 # return HttpResponse(context, request)

class LibraryDetailView(Library):
 def get(self, request):
  self.library_id = request.Library.pk
  self.library = Library.objects.get(pk=self.library_id)
  self.library_books = Book.objects.filter(pk=self.library.books)
  template = loader.get_template('relationship_app/library_detail.html')
  context = {
    'library.books.all': self.library_books,
  }
  return HttpResponse(template.render(context, request))