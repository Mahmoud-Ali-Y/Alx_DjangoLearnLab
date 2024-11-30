from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
    def validate(self, data):
        if data['publication_year'] > 2024:
            raise serializers.ValidationError("Publication Year must not be in the future.")
        return data
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = ['name', 'books']