from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'author_username', 'content', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'author_username', 'created_at', 'updated_at']