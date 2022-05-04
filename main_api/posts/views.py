from msilib.schema import Error
from django.shortcuts import render
from rest_framework.views import APIView 
from .models import PostModel
from rest_framework.response import Response
from .serializers import PostSerializer
# Create your views here.

class PostView(APIView): 
  
  def get(self, request): 
    selectedPost = PostModel.objects.all()
    serializedPosts = PostSerializer(selectedPost, many=True)
    
    return Response(serializedPosts.data)
    
  def post(self, request): 
    new_post_data = request.data 
    new_post = PostModel(**request.data)
    new_post.save()
    
    return Response(new_post_data) 


class PostByIdView(APIView): 
  def get(self, request, postId: int): 
    try: 
      currentPost = PostModel.objects.get(id = postId)
    except: return Response("nothing where found")
    serializedPost = PostSerializer(currentPost)
    
    return Response(serializedPost.data)
  
  def delete(self, request, postId: int): 
    try: 
      deletedPost = PostModel.objects.get(id=postId)
      deletedPost.delete()
    except: return Response("nothing was deleted")
    
    serializedPost = PostSerializer(deletedPost)
    
    return Response(serializedPost.data)
   
  def put(self, request, postId: int): 
    try: 
      updatingPost = PostModel.objects.filter(id = postId).update(**request.data)
    
      return Response(updatingPost)
    except BaseException as error: 
      print(error)
      return Response("invalid data suka")  
    
class SearchPostsView(APIView): 
  def get(self, request): 
    search = request.GET.get("search")
    
    try: 
      searching_posts = PostModel.objects.filter(name__startswith = search)
      
      serialized_posts = PostSerializer(searching_posts, many=True)
      return Response(serialized_posts.data)
    except: return Response("fucking slaves arrived")