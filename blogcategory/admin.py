from django.contrib import admin
from .models import Category, PostCategory, UserFavouriteCategory


class PostCategoryInLine(admin.TabularInline):
    model = PostCategory.category.through


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostCategoryInLine,
    ]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategory)
admin.site.register(UserFavouriteCategory)
