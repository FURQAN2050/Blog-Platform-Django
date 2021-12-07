from django.shortcuts import render
from rest_framework.views import APIView

from blogcomment.serializers import PostCommentSerializer
from .models import PostComment
from rest_framework.response import Response
import json
from authentication.models import User

# Create your views here.
class CreatePostComment(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        payload = json.loads(request.body)
        print(payload)
        author = User.objects.get(id=payload["user_id"])
        post = PostComment.objects.create(
            title=payload["title"],
            content=payload["content"],
            author=author,
            post_id=payload["post_id"],
        )
        print(post)
        return Response({"success": True})


class GetPostComment(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        payload = json.loads(request.body)
        queryset = (
            PostComment.objects.select_related("author")
            .filter(post_id=payload["id"])
            .order_by("-created_at")
            .all()
        )
        data = []
        for i in queryset:
            data.append(
                {
                    "title": i.title,
                    "id": i.id,
                    "title": i.title,
                    "published": i.published,
                    "created_at": i.created_at,
                    "post_id": i.post_id,
                    "content": i.content,
                    "author": {
                        "first_name": i.author.first_name,
                        "last_name": i.author.last_name,
                        "id": i.author.id,
                    },
                }
            )
        return Response({"data": data, "success": True})
