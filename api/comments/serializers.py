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

    def create(self,validated_data):
        user =  self.context['request'].user
        book = validated_data["book"]

        comment = Comment.objects.filter(user=user,book=book)

        if comment:
            raise serializers.ValidationError({"error": "Bu kitaba zaten yorum yaptınız."})
        else:
            return super().create(validated_data)