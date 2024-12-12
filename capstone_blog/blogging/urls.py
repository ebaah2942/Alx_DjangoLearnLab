from django.urls import path
from .views import PostListCreateView, LoginView, LogoutView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]