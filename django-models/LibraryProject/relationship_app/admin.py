from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Book, Library, Librarian, Author

# Register your models here.
class CustomAdminSite(admin.AdminSite):
    def has_permission(self, request):
      
        if not request.user.is_authenticated:
            return False

        try:
            return request.user.userprofile.role == 'Admin'
        except UserProfile.DoesNotExist:
            return False
        

custom_admin_site = CustomAdminSite(name='custom_admin') 

custom_admin_site.register(Book, Library, Librarian, Author)       