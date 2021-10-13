from django.urls import path,include


from .views import BookCreateAPIView,BookListAPIView,BookUpdateAPIView,BookDetailAPIView,BestFiveBookListAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name="books"),
    path('create/', BookCreateAPIView.as_view(), name="create_book"),
    path('update/<id>', BookUpdateAPIView.as_view(), name="update_book"),
    path('detail/<id>', BookDetailAPIView.as_view(), name="detail_book"),
    path('best-five/', BestFiveBookListAPIView.as_view(), name="best_five_books"),
]