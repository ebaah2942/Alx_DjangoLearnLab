from django . urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='book_list'),
    path('LibraryDetailView/<int:pk>/', views.LibraryDetailView.as_view(), name='LibraryDetailView'),
]