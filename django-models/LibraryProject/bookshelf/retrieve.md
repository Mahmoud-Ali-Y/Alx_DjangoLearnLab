specific_book = Book.objects.get(title='1984')
print (f'Title: {specific_book.title}, Author: {specific_book.author}, Publication year: {specific_book.publication_year}')
# Title: 1984, Author: George Orwell, Publication year: 1949