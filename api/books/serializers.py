from rest_framework import serializers

from core.models import Book
from api.comments.serializers import CommentSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'name',
            'writer',
            'get_image',
            'place_of_publication',
            'date_of_publication',
            'publisher',
            'category',
            'summary',
            'rating',
            )
        extra_kwargs = {'author': {'read_only': True}}

class BookDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'name',
            'writer',
            'place_of_publication',
            'date_of_publication',
            'publisher',
            'category',
            'summary',
            'rating',
            'comments',
            )
        extra_kwargs = {'author': {'read_only': True}}
