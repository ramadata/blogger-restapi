from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    """
    model serializers: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    """
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published']


