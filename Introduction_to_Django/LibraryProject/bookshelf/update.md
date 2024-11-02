specific_book = Book.objects.filter(title='1984')
specific_book.update(title='Nineteen Eighty-Four')
# 1