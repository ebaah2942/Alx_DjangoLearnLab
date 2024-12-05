from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name= 'blog/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),


]