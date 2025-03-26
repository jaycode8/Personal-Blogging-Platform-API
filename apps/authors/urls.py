from django.urls import path
from.views import AuthorView

urlpatterns = [
    path("authors", AuthorView.as_view())
]