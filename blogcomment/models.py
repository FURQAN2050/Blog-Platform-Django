from django.db import models
import blog.models as BlogModels

# Create your models here.


class PostComment(models.Model):
    title = models.CharField(max_length=200, unique=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.OneToOneField(BlogModels.Post, on_delete=models.CASCADE)
    content = models.TextField()
