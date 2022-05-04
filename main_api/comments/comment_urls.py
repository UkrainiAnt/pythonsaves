from django.urls import path 
from .comment_views import CommentListView

urlpatterns = [
  path("list", CommentListView.as_view())
]