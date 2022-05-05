from rest_framework import serializers 
from .models import PostModel
from users.user_serializer import UserSerializer


class PostSerializer(serializers.ModelSerializer): 
  user = UserSerializer()
  class Meta: 
    model = PostModel
    fields = "__all__"
    
