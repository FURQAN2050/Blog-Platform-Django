from typing import ParamSpec
from django.contrib import admin
from .models import Post
from .models import TestModel


# Register your models here.
admin.site.register(Post)
admin.site.register(TestModel)