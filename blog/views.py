from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import TestModel
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def test_api(request):
    return HttpResponse('test Api response');

class TestModelViewSet(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = TestModel.objects.all().order_by('name');
        print(queryset);
        return Response(queryset);
    


