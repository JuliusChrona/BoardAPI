from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.SlugField(max_length=255, unique=True)
    creation_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}. {self.title} | author: {self.owner}"

    class Meta:
        ordering = ["-id"]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} | author: {self.user.username}"

    class Meta:
        ordering = ["-id"]


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="upvotes")
    upvote = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} upvote for "{self.post.title}"'

    class Meta:
        unique_together = ["user", "post"]
