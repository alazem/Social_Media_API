from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet  # Import the missing UserProfileViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='profile')
