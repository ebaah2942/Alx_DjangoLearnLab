from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_librarian(user):
    return UserProfile.objects.filter(user=user, role='Librarian').exists()



@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', role='Librarian')
