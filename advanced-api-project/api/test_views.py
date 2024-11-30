from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import *

def setUp(self):
    Author.objects.create(name="lion")
    Book.objects.create(title = 'Forest', publication_year = 2000, author = 'lion' )

def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        book = Book.objects.get(title="Forest")
        self.assertEqual(Book.view())
        self.assertEqual(Book.update())
        self.assertEqual(Book.delete())