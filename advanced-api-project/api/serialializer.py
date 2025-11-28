from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model including custom validation.
    Ensures publication_year cannot be in the future.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model and includes a nested list of BookSerializer.
    Uses the 'books' related_name defined in the Book model.
    """
    books = BookSerializer(many=True, read_only=True)
    

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

