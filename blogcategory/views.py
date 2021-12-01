from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
from rest_framework.response import Response

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
