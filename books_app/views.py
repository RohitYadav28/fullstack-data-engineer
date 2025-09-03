import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class FetchExternalData(APIView):
    def get(self, request):
        # Pull data from a third-party API (e.g., JSONPlaceholder)
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
        # Save to DB as a new Book (simplified mapping)
        Book.objects.create(
            title=data.get('title', 'External Title'),
            author='API Author',
            price=0.00
        )
        return Response({'message': 'Data fetched and saved', 'data': data})