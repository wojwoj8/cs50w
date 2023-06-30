from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    starting_bid = models.FloatField()
    actual_price = models.FloatField(default = None, null = True, blank = True)
    url = models.URLField(blank = True)
    category = models.CharField(blank = True, max_length=64)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="list")
    active = models.BooleanField(default = True)

class Bid(models.Model):
    #start_bid - item id
    bid_item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    actual_bid = models.FloatField(default = None)
    winner = models.ForeignKey(User, default = None, on_delete=models.CASCADE, related_name="win")
    def __str__(self):
        return f"{self.bid_item} {self.actual_bid} {self.winner}"
    
class Comment(models.Model):
    com = models.CharField(max_length=1024)
    item = models.ForeignKey(Listing, default = None, on_delete=models.CASCADE)
    username = models.ForeignKey(User, default = None, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.username}: {self.com}"

class Watchlist(models.Model):
    username = models.ForeignKey(User, default = None, on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, default = None, on_delete=models.CASCADE)
    watched = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.watched}"

