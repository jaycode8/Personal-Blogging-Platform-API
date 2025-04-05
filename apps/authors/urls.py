from django.urls import path
from .views import author_list, AuthorAPIView, AuthorDetail

urlpatterns = [
        path("", author_list),
        path("<uuid:pk>", AuthorDetail.as_view())
]