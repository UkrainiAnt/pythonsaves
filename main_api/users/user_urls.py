from django.urls import path 
from .views import UserView, UserListView, UserSearchView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("list", UserListView.as_view()),
    path("search", UserSearchView.as_view()),
    path("<int:userId>", UserView.as_view()),
    
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify', TokenVerifyView.as_view(), name='token_verify'),
]

