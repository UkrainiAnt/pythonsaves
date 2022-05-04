from django.urls import path 
from .comment_views import CommentListView, CommentByIdView

urlpatterns = [
  path("list", CommentListView.as_view()),
  path("<int:commentId>", CommentByIdView.as_view())
]