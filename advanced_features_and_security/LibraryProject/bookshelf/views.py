from django.shortcuts import render
from .models import *
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
# Create your views here.
@permission_required('app_name.can_edit', raise_exception=True)
def create_book(request):
    new_book = Book.objects.create()