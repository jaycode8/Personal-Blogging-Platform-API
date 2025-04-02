from django.urls import path
from .views import ListCreateArticle, articles_detail, UpdateArticle


urlpatterns = [
    path("", ListCreateArticle.as_view()),
    path("<uuid:id>/", articles_detail),
    path("article/<uuid:pk>", UpdateArticle.as_view()),
]


