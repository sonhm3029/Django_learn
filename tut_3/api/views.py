from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

