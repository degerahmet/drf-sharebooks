from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterAPIView,BlacklistTokenUpdateView,WriterListAPIView,PublisherListAPIView

from django.urls import path, include

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('logout/', BlacklistTokenUpdateView.as_view(), name='logout'),
    path('writers/', WriterListAPIView.as_view(), name='writers'),
    path('publishers/', PublisherListAPIView.as_view(), name='publishers'),

    path('books/', include('api.books.urls')),
    path('comments/', include('api.comments.urls')),
    path('favorites/', include('api.favorites.urls')),
]