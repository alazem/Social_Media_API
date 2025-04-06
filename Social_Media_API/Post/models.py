from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey("User.User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Post by {self.user.username} - {self.created_at}"
