from django.db import models

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"
