from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Follow
from .serializers import FollowSerializer
from User.serializers import UserSerializer  # Import from User.serializers

User = get_user_model()

class FollowersAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        followers = Follow.objects.filter(following=user)
        serializer = FollowSerializer(followers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowingAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        following = Follow.objects.filter(follower=user)
        serializer = FollowSerializer(following, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        to_follow = get_object_or_404(User, id=user_id)
        if request.user == to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(follower=request.user, following=to_follow)
        if not created:
            return Response({"detail": "You already follow this user."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FollowSerializer(follow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnfollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, user_id):
        to_unfollow = get_object_or_404(User, id=user_id)
        follow = Follow.objects.filter(follower=request.user, following=to_unfollow).first()

        if follow:
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)
