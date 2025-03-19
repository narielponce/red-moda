from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass  # Se puede extender si necesitas más atributos

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTE_CHOICES = [(LIKE, 'Like'), (DISLIKE, 'Dislike')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote = models.IntegerField(choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'post')  # Un voto por usuario por post