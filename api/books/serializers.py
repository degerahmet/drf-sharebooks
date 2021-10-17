from rest_framework import serializers

from core.models import Book
from api.comments.serializers import CommentSerializer

class BookSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'name',
            'writer',
            'get_image',
            'image',
            'place_of_publication',
            'date_of_publication',
            'publisher',
            'category',
            'summary',
            'rating',
            )
        extra_kwargs = {'author': {'read_only': True},
        'get_image': {'read_only': True}}
    
    def get_writer(self,obj):
        return obj.writer.name
    
    def get_publisher(self,obj):
        return obj.publisher.title
    
    def get_category(self,obj):
        return obj.category.title

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'author',
            'name',
            'writer',
            'image',
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
    writer = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
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
            'comments',
            )
        extra_kwargs = {'author': {'read_only': True}}
    def get_writer(self,obj):
        return obj.writer.name
    
    def get_publisher(self,obj):
        return obj.publisher.title
    
    def get_category(self,obj):
        return obj.category.title