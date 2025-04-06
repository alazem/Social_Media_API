from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import get_user_model
from Post.models import Post
from User.serializers import UserSerializer
from Post.serializers import PostSerializer

User = get_user_model()

class UserSearchAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        query = request.GET.get('q', '')
        users = User.objects.filter(username__icontains=query)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class PostSearchAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        query = request.GET.get('q', '')
        posts = Post.objects.filter(content__icontains=query)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
