from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.views import generic
from .models import Book
from api.serializers import BookSerializer

# Create your views here.

# Book List class to retrieve all books
class BookList(ListAPIView):
    serializer_class = BookSerializer 

    def get_queryset(self):
        return Book.objects.all()

