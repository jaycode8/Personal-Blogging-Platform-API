from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.

class AuthorView(CreateAPIView):
    serializer_class = AuthorSerializer