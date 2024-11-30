from django.test import TestCase 
from rest_framework.test import APIRequestFactory
from .models import *
from .views import *
from rest_framework import status

class APITestCase:
 def setUp(self):
     Author.objects.create(name="lion")
     Book.objects.create(title = 'Forest', publication_year = 2000, author = 'lion' )

 def test_books_can_updated(self):
         """Animals that can speak are correctly identified"""
         book = Book.objects.get(title="Forest")
         self.assertEqual(Book.view())
         self.assertEqual(Book.update())
         self.assertEqual(Book.delete())
class UrlTests(TestCase):
    
    def get_url():
     factory = APIRequestFactory()
     request = factory.get('/api/books/')
     response = CustomBookListView(request)
     return response.data