from django.db import models

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey("User.User", on_delete=models.CASCADE)
    post = models.ForeignKey("Post.Post", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"
