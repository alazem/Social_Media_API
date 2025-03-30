from rest_framework.routers import DefaultRouter
from .views import LikeViewSet  # Import LikeViewSet from the views module

router = DefaultRouter()
router.register(r'likes', LikeViewSet, basename='like')
