from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer
from django.shortcuts import render


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def home(request):
    return render(request, 'index.html')


