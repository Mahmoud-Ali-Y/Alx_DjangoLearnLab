from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer # replace with your project's serializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters

# Create your views here.
class CustomBookCreateView(generics.CreateAPIView):
# can be any name, ensure to align with your project as this is sample exampls 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CustomBookListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'publication_year', 'author']
    ordering_fields = ['title', 'publication_year', 'author']


    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        title = self.request.title
        return Book.objects.filter(title=title)

class CustomBookDetailView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomBookUpdateView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomBookDeleteView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer