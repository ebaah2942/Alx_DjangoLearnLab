from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.views import generic
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.

# Book List class to retrieve all books
class BookList(generic.ListView):
    serializer_class = BookSerializer 

    def get_queryset(self):
        return Book.objects.all()

# DRF built in view to retrieve all books
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer