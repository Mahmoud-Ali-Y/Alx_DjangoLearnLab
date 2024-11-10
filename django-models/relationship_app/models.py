from django.db import models

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