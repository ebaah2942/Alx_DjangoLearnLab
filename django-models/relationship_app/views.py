from django.shortcuts import render
from . models import Book
from django.views.generic import DetailView
from . models import Library

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class BookListView(DetailView):
    model = Book
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.objects.books.all()
        return context


