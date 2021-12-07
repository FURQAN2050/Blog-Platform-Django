from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView

from blog.serializers import PostSerializer
from .models import Post, TestModel
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from authentication.models import User

# Create your views here.


def test_api(request):
    return HttpResponse("test Api response")


class TestModelViewSet(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = TestModel.objects.all().order_by("name")
        print(queryset)
        return Response(queryset)


class GetAllBlogs(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        queryset = Post.objects.all().values()
        # print(queryset)
        return Response(queryset)


class CreateBlog(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        payload = json.loads(request.body)
        author = User.objects.get(id=payload["author_id"])
        success = False
        print(author)
        post = Post.objects.create(
            title=payload["title"],
            slug=payload["slug"],
            content=payload["content"],
            status=payload["status"],
            author=author,
        )
        serializer = PostSerializer(post)
        print(post)
        return Response({"data": serializer.data, "success": True})


class GetBlog(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        payload = json.loads(request.body)
        user = payload["user_id"]
        is_liked = False
        postObj = get_object_or_404(Post, id=payload["id"])
        if postObj.likes.filter(id=user).exists():
            is_liked = True
        post = Post.objects.filter(id=payload["id"]).values()
        print(post)
        return Response({"success": True, "post": post, "is_liked": is_liked})
        # return Response({is_liked:is_liked})


class likeBlog(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        print("appi fit")
        # print(request.get("post_id"))
        # print(request.POST.get("post_id"))
        is_liked = False
        payload = json.loads(request.body)
        user = payload["user_id"]
        print(user)
        post = get_object_or_404(Post, id=payload["post_id"])
        if post.likes.filter(id=user).exists():
            post.likes.remove(user)
            is_liked = False
        else:
            print(post)
            post.likes.add(user)
            is_liked = True
        return Response({"success": True})


class getUserProfile(APIView):
    def post(self, request):
        payload = json.loads(request.body)
        user = payload["user_id"]
        payload = json.loads(request.body)
        author = User.objects.filter(id=user).values()
        posts = Post.objects.filter(author=user).values()
        postsCount = Post.objects.filter(author=user).count()

        return Response(
            {
                "success": True,
                "user": author,
                "authorPost": posts,
                "postCount": postsCount,
            }
        )
