from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user)
    notificaton_list = [
        {
            'id': notification.id,
            'verb': notification.verb,
            'actor': notification.actor.username,
            'timestamp': notification.timestamp,
            'target_id': notification.target_object_id
        } for notification in notifications

    ]
    return JsonResponse({'notifications': notificaton_list})

@login_required
def mark_notifications_as_read(request):
    notifications = Notification.objects.filter(recipient=request.user)
    for notification in notifications:
        notification.read = True
        notification.save()
    return JsonResponse({'success': True})
