from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CommentSerializer, PostSerializer
from .models import Post, Comment, Like
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            recipient = post.author,
            actor = request.user,
            verb = 'Liked your post',
            target = post
        )

    return JsonResponse({'success': True, 'likes_count': post.likes.count()})
@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post).first()
    if like:
        like.delete()
    return JsonResponse({'success': True, 'likes_count': post.likes.count()})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
     # Fetch posts from followed users
    following_users = request.user.following.all()
    if not following_users.exists():
        return Response({"message": "You are not following anyone yet."}, status=200)

    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    # Paginate posts
    paginator = PostPagination()
    paginated_posts = paginator.paginate_queryset(posts, request)

    # Serialize and return paginated data
    serializer = PostSerializer(paginated_posts, many=True)
    return paginator.get_paginated_response(serializer.data)
   

class IsOwnerOrReadOnly(permissions.BasePermission):
    # custom permission to allow only author to edit and delete a post or comment
    def has_object_permissions(self, request, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions are only allowed to the author
        is_owner = obj.author == request.user
        if not is_owner:
            print(f"Permission denied: {request.user} is not the owner of the post")
        return is_owner
    
class PostPagination(PageNumberPagination):
    page_size = 10
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']
    pagination_class = PostPagination

    def perform_create(self, serializer):
        # This authomatically sets the author to the current user
        serializer.save(author=self.request.user)    


class CommentPagination(PageNumberPagination):
    page_size = 5
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CommentPagination


    def perform_create(self, serializer):
       
        comment = serializer.save(user=self.request.user)

        # Create a notification for the post's author
        post = comment.post
        if post.author != self.request.user:  # Avoid notifying the author if they comment on their own post
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb='commented on your post',
                target=post
            )


