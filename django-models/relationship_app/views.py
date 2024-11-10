from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
def list_books(request):
  books = Book.objects.all().values()
  template = loader.get_template('relationship_app/list_books.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))
 # return HttpResponse(context, request)

class LibraryDetailView(DetailView):
 model = Library
 def get(self, request, id):
 # self.library_id = request.Library.pk
  self.library = Library.objects.get(pk=id)
 # self.library_books = Book.objects.filter(pk=self.library.books)
  template = loader.get_template('relationship_app/library_detail.html')
  context = {
    'library.books.all': self.library.books.all(),
  }
  return HttpResponse(template.render(context, request))
 
 class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'