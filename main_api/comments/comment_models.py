from django.db import models
from users.models import UserModel
from posts.models import PostModel
# Create your models here.

class CommentModel(models.Model): 
  body = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True)
  user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
  