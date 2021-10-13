from django.urls import path,include


from .views import FavoriteCreateAPIView,FavoriteBooksGetAPIView

urlpatterns = [
    path('add/', FavoriteCreateAPIView.as_view(), name="add_favorite"),
    path('', FavoriteBooksGetAPIView.as_view(), name="get_favorites"),
]