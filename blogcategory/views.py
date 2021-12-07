from django.shortcuts import render
from rest_framework.views import APIView

from authentication.models import User
from .models import Category, UserFavouriteCategory
from rest_framework.response import Response
import json

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.http import JsonResponse
# from django.core.serializers import serialize


class GetAllBlogs(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Category.objects.all().values()
        print(queryset)
        return Response(queryset)


class postFavouriteCategories(APIView):
    def post(self, request):
        success = True
        payload = json.loads(request.body)
        categories = payload["data"]
        print(categories)
        for category in categories:
            print(category["user_id"])
            isAlreadyExist = UserFavouriteCategory.objects.filter(
                user_id=category["user_id"], category_id=category["category_id"]
            ).exists()
            if isAlreadyExist == False:
                print(isAlreadyExist)
                UserFavouriteCategory.objects.create(
                    category_id=category["category_id"], user_id=category["user_id"]
                )
            # else:
            #     res=UserFavouriteCategory.objects.filter(user_id=category["user_id"], category_id=category["category_id"])

        return Response({"success": success})


class getFavouriteCategories(APIView):
    def post(self, request):
        success = True
        payload = json.loads(request.body)
        records = UserFavouriteCategory.objects.filter(
            user_id=payload["user_id"]
        ).values()
        return Response({"success": success, "data": records})
