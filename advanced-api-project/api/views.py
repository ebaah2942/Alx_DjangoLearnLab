from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django_filters import rest_framework
from rest_framework import generics



# Create your views here.
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # Filter by title, author, and publication year for large datasets
    filterset_fields = ['title', 'author', 'publication_year']
    # Search by title and author for easy navigation
    search_fields = ['title', 'author']
    # Order by publication year and title, this helps in sortind data efficiently
    ordering_fields = ['publication_year', 'title']
    ordering = [ 'title']


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

