from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from .serializers import PostSerializer

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class PostList(APIView):
    """
    lists posts or create a new post
    """
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        """
        renders to content type as requested by client
        """
        posts       = Post.objects.all()
        serializer  = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    read, update, or delete an individual post
    """

    def get_post(self, key):
        try:
            return Post.objects.get(key=key)
        except:
            raise Http404
    def get(self, request, key,format=None):
        post = self.get_post(key)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, key, format=None):
        post = self.get_post(key)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, key, format=None):
        post = self.get_post(key)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


