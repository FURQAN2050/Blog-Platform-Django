from django.db import models
import blog.models as BlogModels

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    metaTitle = models.CharField(max_length=200, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ManyToManyField(BlogModels.Post)
    category = models.ManyToManyField(Category)
