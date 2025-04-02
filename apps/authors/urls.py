from django.urls import path
from .views import author_list, AuthorAPIView

urlpatterns = [
        path("", author_list),
        path("<uuid:pk>", AuthorAPIView.as_view())
]