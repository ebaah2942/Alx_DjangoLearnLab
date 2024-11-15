from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse

def is_librarian(user):
    return user.userprofile.role == 'Librarian'




@user_passes_test(is_librarian)
def librarian_view(request):
    # return render(request, 'relationship_app/librarian_view.html')
    return HttpResponse("Welcome, Librarian!")
