from rest_framework import serializers
from .models import Author, Book

# Serialized the name field from Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Indicates that this field will handle multiple related objects 
    # (e.g., many books for one author).
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']
    


# Serialized the Book model for all the fields
class BookSerializer(serializers.ModelSerializer):
    # This dynamivally adds the related_books field and serializes it
    related_books = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'    

    # This method serializes the related_books field
    def get_related_bbooks(self, obj):
        if obj.related_books.exists():
            return BookSerializer(obj.related_books.all(), many=True).data
        return None
    
    
    # This method validates the publication year
    def validate_publication_year(self, value):
        if value > 2024:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value 