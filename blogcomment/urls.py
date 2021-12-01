from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URL Conf Module.
urlpatterns = [
    path("api/GetPostComment/", views.GetPostComment.as_view()),
    path("api/addPostComment/", views.CreatePostComment.as_view()),
]
