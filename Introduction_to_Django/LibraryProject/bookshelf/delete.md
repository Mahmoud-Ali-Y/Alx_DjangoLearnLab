book_to_deleted = Book.objects.get(title='Nineteen Eighty-Four')
book_to_deleted.delete()
# (1, {'bookshelf.Book': 1})