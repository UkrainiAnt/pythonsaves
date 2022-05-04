from django.db import models

# Create your models here.

class CommentModel(models.Model): 
  body = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  