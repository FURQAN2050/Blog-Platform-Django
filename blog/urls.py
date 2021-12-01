from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URL Conf Module.
urlpatterns = [
    path("api/test/", views.test_api),
    path("api/getBlogs/", views.GetAllBlogs.as_view()),
    path("api/getBlog/", views.GetBlog.as_view()),
    path("api/createBlog/", views.CreateBlog.as_view()),
    path("testModel/", views.TestModelViewSet.as_view()),
]
