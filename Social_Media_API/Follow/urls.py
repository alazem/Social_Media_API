from rest_framework.routers import DefaultRouter
from .views import FollowViewSet  # Import FollowViewSet from the views module

router = DefaultRouter()
router.register(r'follows', FollowViewSet, basename='follow')
