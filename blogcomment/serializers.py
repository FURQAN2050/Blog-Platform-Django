from .models import PostComment
from rest_framework import serializers


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = [
            "id",
            "title",
            "published",
            "created_at",
            "post_id",
            "content",
            "author",
        ]
