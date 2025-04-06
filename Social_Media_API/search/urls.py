from django.urls import path
from .views import UserSearchAPIView, PostSearchAPIView

urlpatterns = [
    path('users/', UserSearchAPIView.as_view(), name='search-users'),
    path('posts/', PostSearchAPIView.as_view(), name='search-posts'),
]
