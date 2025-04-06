# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # Assuming 'user' is the correct field name in your model
    author_username = serializers.CharField(source='user.username', read_only=True)  # Adjusting to 'user'

    class Meta:
        model = Post
        fields = ['id', 'user', 'author_username', 'content', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'author_username', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Ensure the user field is assigned to the logged-in user
        user = self.context['request'].user  # Get the logged-in user from the request context
        post = Post.objects.create(user=user, **validated_data)  # Create the post with the logged-in user
        return post
