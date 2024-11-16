from django.contrib import admin
from .models import Book
from .models import CustomUser
from .models import CustomUserAdmin
from django.contrib.auth.admin import UserAdmin

# class BookAdmin(admin.ModelAdmin):
#     list_filter = ('title', 'author', 'publication_year')
#     search_fields = ('title', 'author')

# admin.site.register(Book, BookAdmin)

# Register your models here.

# class UserAdmin(BaseUserAdmin):
#     list_display = ['date_of_birth', 'profile_photo', 'is_staff', 'is_superuser']

# admin.site.register(CustomUser, CustomUserAdmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)