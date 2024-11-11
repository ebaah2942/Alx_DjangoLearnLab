from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile


def is_member(user):
    return UserProfile.objects.filter(user=user, role='Member').exists()


@user_passes_test(is_member)
def member_view(request):    
    return render(request, 'relationship_app/member_view.html', role='Member')