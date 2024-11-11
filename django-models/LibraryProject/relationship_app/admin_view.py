from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_admin(user):
    return UserProfile.objects.filter(user=user, role='Admin').exists()


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', role='Admin')