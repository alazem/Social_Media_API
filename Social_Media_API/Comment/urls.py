from django.urls import path
from Comment.views import CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:comment_id>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]
    