from rest_framework import serializers

from core.models import Book

class BookSerializer(serializers.ModelSerializer):
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
            )
        extra_kwargs = {'author': {'read_only': True}}
