from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField("User.User", on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

