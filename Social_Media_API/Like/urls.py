from django.urls import path
from .views import PostLikesAPIView, LikePostAPIView, UnlikePostAPIView

urlpatterns = [
    path('posts/<int:post_id>/likes/', PostLikesAPIView.as_view(), name='post-likes'),
    path('posts/<int:post_id>/like/', LikePostAPIView.as_view(), name='post-like'),
    path('posts/<int:post_id>/unlike/', UnlikePostAPIView.as_view(), name='post-unlike'),
]
