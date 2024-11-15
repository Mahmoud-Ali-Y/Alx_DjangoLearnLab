from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.decorators import user_passes_test
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
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def has_perm(self, perm, obj=None):
    try:
        user_perm = self.Book_permissions.get(codename=perm)
    except ObjectDoesNotExist:
        user_perm = False
    if user_perm:
        return True
    else:
        return False
    @permission_required('relationship_app.can_add_book', login_url="/login/")
    def add_book():
      newbook = Book.objects.create()
    @permission_required('relationship_app.can_change_book', login_url="/login/")
    def change_book():
      book = Book.objects.get(id=1)
      book.name = ''
    @permission_required('relationship_app.can_delete_book', login_url="/login/")
    def delete_book():
      book = Book.objects.get(id=1)
      book.delete
    def check_role(function):
      def wrap(request, id):
        user_profile = UserProfile.objects.get(id = id)
        match user_profile.role:
          case 'Admin':
            return admin_view(request, id)
          case 'Librarian':
            return librarian_view(request, id)
          case 'Member':
            return member_view(request, id)
    @check_role
    def admin_view(request, id):
     user = UserProfile.objects.get(id=id)
     if user.role == 'Admin':
      template = loader.get_template('relationship_app/Admin.html')
      return HttpResponse(template.render())
    @check_role
    def librarian_view(request):
     user = UserProfile.objects.get(id=id)
     if user.role == 'Librarian':
      template = loader.get_template('relationship_app/Librarian.html')
      return HttpResponse(template.render())
    @check_role
    def member_view(request):
     user = UserProfile.objects.get(id=id)
     if user.role == 'Member':
      template = loader.get_template('relationship_app/Member.html')
      return HttpResponse(template.render())