from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveDestroyAPIView
from .serializers import AuthorSerializer
from .models import Author

class AuthorAPIView(RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@api_view(["GET", "POST"])
def author_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})
    
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AuthorDetail(APIView):
    def get_object(request, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)



