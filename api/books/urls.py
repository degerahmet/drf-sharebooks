from django.urls import path,include


from .views import CreateBookAPIView,BookListAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name="books"),
    path('create/', CreateBookAPIView.as_view(), name="create_book"),

]