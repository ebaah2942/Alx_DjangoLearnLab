from .models import Comment, Post
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    # This field serializes the author field of the Post model into a string representation instead of the default primary key (ID).
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    # 
    author = serializers.StringRelatedField(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']


