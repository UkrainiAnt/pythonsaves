from rest_framework import serializers
from .comment_models import CommentModel
from posts.serializers import PostSerializer
from users.user_serializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer): 
  post = PostSerializer()
  user = UserSerializer()
  
  class Meta: 
    model = CommentModel 
    fields = "__all__"