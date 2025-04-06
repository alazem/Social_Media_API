from django.db import models

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey("comment.Comment", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'post', 'comment')
    def __str__(self):
        if self.post:
            return f"{self.user.username} liked Post {self.post.id}"
        return f"{self.user.username} liked Comment {self.comment.id}"
