from django.urls import path,include


from .views import BookCreateAPIView,BookListAPIView,BookUpdateAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name="books"),
    path('create/', BookCreateAPIView.as_view(), name="create_book"),
    path('update/<id>', BookUpdateAPIView.as_view(), name="update_book"),

]