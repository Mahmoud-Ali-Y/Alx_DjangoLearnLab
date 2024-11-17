from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self): 
      return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    class Meta(type):
        permissions = ("can_add_book", "can_change_book", "can_delete_book")
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='books')
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    def create_user(self):
        user = CustomUser.objects.create_user(self.date_of_birth, self.profile_photo)
    def create_superuser(self):
        user = CustomUser.objects.create_superuser(self.date_of_birth, self.profile_photo)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = ("Admin", "Librarian", "Member")
    role = models.CharField(max_length=1, choices=role_choices)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

#class CustomUserManager(AbstractUser):
#    date_of_birth = models.DateField()
#    profile_photo = models.ImageField()