from rest_framework.routers import DefaultRouter
from .views import PostViewSet  # Import PostViewSet from the views module

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
