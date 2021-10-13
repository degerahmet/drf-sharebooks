from rest_framework import serializers
from core.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'book',
            'user',
            'comment',
            'rate'
            )
        extra_kwargs = {'user': {'read_only': True}}
