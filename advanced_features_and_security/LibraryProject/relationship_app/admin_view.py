from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse


def is_admin(user):
    # return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # return render(request, 'relationship_app/admin_view.html')
    return HttpResponse("Welcome, Admin!")