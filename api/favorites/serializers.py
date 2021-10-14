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
    
    def create(self,validated_data):
        user =  self.context['request'].user
        book = validated_data["book"]

        favorite = Favorite.objects.filter(user=user,book=book)

        if favorite:
            raise serializers.ValidationError({"error": "Bu kitap zaten favorilere eklendi"})
        else:
            return super().create(validated_data)

