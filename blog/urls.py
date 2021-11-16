from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URL Conf Module.
urlpatterns=[
    path('api/test/',views.test_api),
    path('testModel/',views.TestModelViewSet.as_view())
]