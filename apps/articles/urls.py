from django.urls import path
from .views import ListCreateArticle, articles_detail


urlpatterns = [
    path("", ListCreateArticle.as_view()),
    path("<uuid:id>/", articles_detail),
]


