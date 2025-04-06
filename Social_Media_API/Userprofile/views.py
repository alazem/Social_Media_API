from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user.pk != self.get_object().pk:
            raise PermissionDenied("You can only update your own profile.")
        serializer.save()

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user.pk != instance.pk:
            raise PermissionDenied("You can only delete your own account.")
        instance.delete()
