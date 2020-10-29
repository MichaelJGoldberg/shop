from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    genre = models.CharField(max_length=25)
    price = models.IntegerField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    texts = models.TextField()
    game = models.ForeignKey(Game,related_name='comments',on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)
    def __str__(self):
        return self.texts