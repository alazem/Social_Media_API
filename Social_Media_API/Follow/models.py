from django.db import models

# Create your models here.
class Follow(models.Model):
    follower = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['follower', 'following']
        
    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
