from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from .models import Article
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

class UpdateArticle(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ListCreateArticle(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def articles_detail(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)


