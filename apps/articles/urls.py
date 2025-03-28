from django.urls import path
from .views import ListCreateArticle

urlpatterns = [
    path("", ListCreateArticle.as_view())
]


