from .views import PostView, PostByIdView, SearchPostsView
from django.urls import path

urlpatterns = [
  path("list", PostView.as_view()),
  path('search', SearchPostsView.as_view()),
  path("<int:postId>", PostByIdView.as_view())
 
]