from bookshelf.models import Book
# create 
new_book = Book(title='1984', author='George Orwell', publication_year='1949')
new_book.save()
# retrieve
specific_book = Book.objects.get(title='1984')
print (f'Title: {specific_book.title}, Author: {specific_book.author}, Publication year: {specific_book.publication_year}')
# Title: 1984, Author: George Orwell, Publication year: 1949
# update
specific_book = Book.objects.filter(title='1984')
specific_book.update(title='Nineteen Eighty-Four')
# 1
# delete
book_to_deleted = Book.objects.get(title='Nineteen Eighty-Four')
book_to_deleted.delete()
# (1, {'bookshelf.Book': 1})