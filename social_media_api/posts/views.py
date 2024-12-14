from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CommentSerializer, PostSerializer
from .models import Post, Comment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
     # Fetch posts from followed users
    followed_users = request.user.following.all()
    posts = Post.objects.filter(user__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
   

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
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
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
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    pagination_class = CommentPagination


    def perform_create(self, serializer):
        # This authomatically sets the author to the current user
        serializer.save(author=self.request.user)



