from django.contrib import admin
from .models import Author, Book
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Book)
class BoookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publication_year']    