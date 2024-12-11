from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView, CommentCreateView)

urlpatterns = [
    path('login/home/', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name= 'blog/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment_to_post'),
    path('search/', views.search, name='search'),
    # path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tag_posts'),
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),



] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)