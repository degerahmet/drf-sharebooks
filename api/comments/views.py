
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import CommentSerializer
from core.models import Book


class CommentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer
