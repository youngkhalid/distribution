from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User)


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey()

