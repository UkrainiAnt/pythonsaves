from django.db import models
from users.models import UserModel

# Create your models here.

class PostModel(models.Model): 
  name = models.CharField(max_length=100)
  subtitle = models.CharField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  image = models.URLField(max_length=100)
  user = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE)
  