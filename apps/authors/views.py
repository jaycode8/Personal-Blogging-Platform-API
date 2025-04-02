from django.http import JsonResponse
from rest_framework.decorators import api_view
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
        # get all authors, serialize them, return json
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse({"authors": serializer.data})
    
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


