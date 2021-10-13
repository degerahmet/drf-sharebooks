from django.urls import path,include


from .views import CommentCreateAPIView

urlpatterns = [
    path('create/', CommentCreateAPIView.as_view(), name="create_comment"),
]