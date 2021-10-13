from rest_framework import serializers
from core.models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = (
            'id',
            'book',
            'user',
            )
        extra_kwargs = {'user': {'read_only': True}}
