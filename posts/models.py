from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)


class Content(models.Model):
    type = models.CharField(max_length=250)
    value = models.TextField()
    post = models.ForeignKey(Post, related_name='content', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.type)
