from django.db import models
import blog.models as BlogModels
from authentication.models import User

# Create your models here.


class PostComment(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post_id = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
