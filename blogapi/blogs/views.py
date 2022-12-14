from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

# Create your views here.
from .serializers import PostSerializer
from .models import Post
from .permissions import IsCustomAuthPermission

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCustomAuthPermission,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer