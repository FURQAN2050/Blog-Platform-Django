from django.shortcuts import render
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
from django.contrib.auth.models import User

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
        queryset = Post.objects.all().values()
        print(queryset)
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
        queryset = Post.objects.filter(id=payload["id"]).values()
        print(queryset)
        return Response(queryset)
