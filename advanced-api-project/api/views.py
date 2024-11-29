from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .permissions import IsAdminOrReadOnly
# Create your views here.
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can create a book
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    # Check if the publication year is in the future before creating the book
    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > 2024:
            raise ValidationError({"publication_year": "Book cannot be published in the future"})
        serializer.save()


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Authenticated users can update their own books and read-only users can only read
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Check if the title is not empty before updating the book
    def perform_update(self, serializer):
        title = serializer.validated_data['title']
        if not title or title.strip() == "":
            raise ValidationError({"title": "Title cannot be empty"})
        serializer.save()



    


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Authenticated users can delete their own books and read-only users can only read
    permission_classes = [IsAuthenticated]        

