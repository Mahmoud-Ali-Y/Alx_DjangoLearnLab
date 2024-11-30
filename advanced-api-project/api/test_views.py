from django.test import TestCase 
from rest_framework.test import APIRequestFactory
from .models import *

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