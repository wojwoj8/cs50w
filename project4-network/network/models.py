from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers_nr = models.IntegerField(default = 0)
    follows_nr = models.IntegerField(default = 0)
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=500)
    post_date = models.DateTimeField()
    likes = models.ManyToManyField(User, blank=True,related_name='like')

    def serialize(self):
        return {
            "id": self.id,
            "post": self.post,
            "post_date": self.post_date,
            "likes": self.likes.count(),
        }

    def __str__(self):
        return f"User: {self.user} Date: {self.post_date}"
    
class Follow(models.Model):
    #person that is followed
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    #follower
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")

    def __str__(self):
        return f"User: {self.username} is followed by: {self.follower}"