from django.contrib import admin
from .models import Book
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class BookAdmin(admin.ModelAdmin):
#     list_filter = ('title', 'author', 'publication_year')
#     search_fields = ('title', 'author')

# admin.site.register(Book, BookAdmin)

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ['date_of_birth', 'profile_photo', 'is_staff', 'is_superuser']

admin.site.register(User, UserAdmin)