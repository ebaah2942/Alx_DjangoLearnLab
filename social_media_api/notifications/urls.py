from django.urls import path
from .views import fetch_notifications, mark_notifications_as_read


urlpatterns = [
    path('notifications/', fetch_notifications, name='notifications'),
    path('notification/<int:notification_id>/seen/', mark_notifications_as_read, name='mark_as_read'),
]