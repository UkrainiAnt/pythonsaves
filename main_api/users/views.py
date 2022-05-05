# Create your views here.
from unicodedata import name
from .user_serializer import UserSerializer
from .user_serializer import UserModel
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .user_serializer import UserSerializer

class UserView(APIView): 
  def get(self, request, userId: int):
    
    currentUser = UserModel.objects.get(id=userId)
    return Response(currentUser)

  def put(self, request, userId: int): 
    updatedUser = UserModel.objects.get(id=userId)
    serializedUser = UserSerializer(updatedUser)
    serializedUser.data.update(name=request.data["name"])
    
    return Response(serializedUser.data)
  
  @permission_classes(IsAdminUser)
  def delete(self, request, userId: int): 
    deleted_user = UserModel.objects.delete(id = userId)
    
    serialized_user = UserSerializer(deleted_user)
    
    return Response(serialized_user.data)
  
class UserListView(APIView): 
  def get(self, request): 
    all_users = UserModel.objects.all()
    
    serialized_users = UserSerializer(all_users, many=True)
    
    return Response(serialized_users.data)  


class UserSearchView(APIView): 
  def get(self, request): 
    search = request.GET.get("search")
    permission_classes = [IsAuthenticated]
     
    try: 
      searching_users = UserModel.objects.filter(email__startswith = search)
      
      serialized_users = UserSerializer(searching_users, many=True)
      return Response(serialized_users.data)
    except: return Response("fucking slaves arrived") 