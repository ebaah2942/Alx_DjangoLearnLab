from django.contrib import admin
from .models import Book, Author

# Register your models here.

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publication_year']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):    
    list_display = ['id', 'name', 'books']