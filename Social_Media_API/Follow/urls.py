from django.urls import path
from .views import (
    FollowersAPIView,
    FollowingAPIView,
    FollowUserAPIView,
    UnfollowUserAPIView,
)

urlpatterns = [
    path('users/<int:user_id>/followers/', FollowersAPIView.as_view(), name='user-followers'),
    path('users/<int:user_id>/following/', FollowingAPIView.as_view(), name='user-following'),
    path('users/<int:user_id>/follow/', FollowUserAPIView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserAPIView.as_view(), name='unfollow-user'),
]
