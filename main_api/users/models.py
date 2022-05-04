from django.db import models

# Create your models here.

userAvatar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiCoHLktPNbzYjYcrFoYnlmxX5SfRKCIJQsA&usqp=CAU"

class UserModel(models.Model): 
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  picture = models.URLField(default=userAvatar)
