
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny

from .serializers import FavoriteSerializer
from core.models import Favorite


class FavoriteCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer


class FavoriteBooksGetAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user)
        return queryset
