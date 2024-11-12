from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views
from django.contrib.auth import views as auth_views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from django.shortcuts import redirect


urlpatterns = [
    path('list_books/', views.list_books, name='book_list'),
    path('LibraryDetailView/<int:pk>/', views.LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
     path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('book_delete/<int:pk>/', views.delete_book, name='delete_book'),


]