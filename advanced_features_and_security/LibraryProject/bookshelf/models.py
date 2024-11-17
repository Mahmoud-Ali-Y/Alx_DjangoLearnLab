from django.db import models
from django.contrib.auth.models import User, AbstractUser
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    def create_user(self):
        user = CustomUser.objects.create_user(self.date_of_birth, self.profile_photo)
    def create_superuser(self):
        user = CustomUser.objects.create_superuser(self.date_of_birth, self.profile_photo)