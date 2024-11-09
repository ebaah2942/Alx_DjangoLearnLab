from django . urls import path
from . import views

urlpatterns = [
    path('book_list/', views.list_books, name='book_list'),
    path('library_list/<int:pk>/', views.LibraryListView.as_view(), name='library_list'),
]