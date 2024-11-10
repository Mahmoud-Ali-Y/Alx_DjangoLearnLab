from .models import *
# Query all books by a specific author.
author_name = pass
author = Author.objects.get(name=author_name)
author_books = Book.objects.filter(author=author)

# List all books in a library.
# library_books = Library.objects.filter(name = '')
# library_books_details = Book.objects.filter(book = library_books)
library_name = pass
books = Library.objects.get(name=library_name)
books.all()
# Retrieve the librarian for a library.
library = Library.objects.get(name=library_name)
library_librarian = Librarian.objects.get(library=library)