from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    can_view_permission = Permission.objects.create(
    codename="can_view",
    name="Can view books",
    )
    can_create_permission = Permission.objects.create(
    codename="can_create",
    name="Can create books",
    )
    can_edit_permission = Permission.objects.create(
    codename="can_edit",
    name="Can edit books",
    )
    can_delete_permission = Permission.objects.create(
    codename="can_delete",
    name="Can delete books",
    )
# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    def create_user(self):
        user = CustomUser.objects.create_user(self.date_of_birth, self.profile_photo)
    def create_superuser(self):
        user = CustomUser.objects.create_superuser(self.date_of_birth, self.profile_photo)
class CustomUserManager(BaseUserManager):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    def create_user(date_of_birth, profile_photo):
        user = CustomUser.objects.create_user(date_of_birth, profile_photo)
    def create_superuser(date_of_birth, profile_photo):
        user = CustomUser.objects.create_superuser(date_of_birth, profile_photo)
class Editors(Group):
    description = models.TextField(blank=True)
 #   group = Group.objects.create(name='Editors')
    group = Group.objects.get(name='Editors')
    group.permissions.add(Book.can_view_permission, Book.can_create_permission, Book.can_edit_permission)