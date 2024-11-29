from .models import Book, Author
from rest_framework import serializers



# This bookselizer serialises the Book model with all the field
class BookSerializer(serializers.ModelSerializer):
    # Allow custom logic to be applied to the related books
    related_books = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
    
    
    # This dynamically retreives and serializes the related books
    def get_books(self, obj):
        if obj.related_books.exists():
            # If there are related books this serializes them
            return BookSerializer(obj.related_books.all(), many=True).data
        return[]



# This authorserialiser serialises the Author model with the field name
class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Author  
        fields = ['name']        