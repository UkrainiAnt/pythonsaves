# Create your views here.
from unicodedata import name
from .serializers import UserSerializer
from .models import UserModel
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.core.exceptions import BadRequest

class UserView(APIView): 
  def get(self, request, userId: int):
    
    currentUser = UserModel.objects.get(id=userId)
    return Response(currentUser)
  
  def put(self, request, userId: int): 
    updatedUser = UserModel.objects.get(id=userId)
    serializedUser = UserSerializer(updatedUser)
    serializedUser.data.update(name=request.data["name"])
    
    return Response(serializedUser.data)
  
  def delete(self, request, userId: int): 
    deleted_user = UserModel.objects.delete(id = userId)
    
    return Response(deleted_user)
  
class UserListView(APIView): 
  def get(self, request): 
    all_users = UserModel.objects.all()
    
    return Response(all_users)  
  
  def post(self, request): 
    serialized_user = UserSerializer(data=request.data)
   
    if serialized_user.is_valid():
      newUser = UserModel.objects.create(**serialized_user.data)
      
      return Response(newUser)
    
    return None
  