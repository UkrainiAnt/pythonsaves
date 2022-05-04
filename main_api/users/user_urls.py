from django.urls import path 
from .views import UserView, UserListView

urlpatterns = [
    path("list", UserListView.as_view()),
    path("<int:userId>", UserView.as_view()),
]