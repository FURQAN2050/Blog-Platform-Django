from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# URL Conf Module.
urlpatterns = [
    path("api/getCategories/", views.GetAllBlogs.as_view()),
]
