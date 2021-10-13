
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .serializers import BookSerializer,BookDetailSerializer
from core.models import Book
from api.permissions import IsContentAuthor


class BookCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer



class BookListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    search_fields =['name']

    filter_backends = [SearchFilter]
    filterset_fields = ['category','writer','publisher']
    queryset = Book.objects.all()



class BookUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsContentAuthor]

    lookup_field = 'id'

class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]

    lookup_field = 'id'

class BestFiveBookListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by("-rating")[:5]