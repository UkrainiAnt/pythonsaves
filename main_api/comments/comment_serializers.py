from rest_framework import serializers
from .comment_models import CommentModel
from posts.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer): 
  post = PostSerializer()
  
  class Meta: 
    model = CommentModel 
    fields = "__all__"