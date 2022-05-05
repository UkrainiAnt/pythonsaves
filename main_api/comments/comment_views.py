from .comment_serializers import CommentSerializer
from .comment_models import CommentModel
from rest_framework.views import APIView 
from rest_framework.response import Response
from posts.models import PostModel
from users.models import UserModel

class CommentListView(APIView): 
  def get(self, request): 
    try: 
      comments = CommentModel.objects.all().select_related("post")
      serialized_comments = CommentSerializer(comments, many=True)  
      
      return Response(serialized_comments.data)
    except Exception as error: 
      print(error)
      return Response("something went wrong")
    
  def post(self, request): 
    try:       
      new_comment = CommentModel.objects.create(body = request.data["body"])
      
      related_post = PostModel.objects.get(id = request.data["post"])
      current_user = UserModel.objects.get(email = request.user)
      
      new_comment.post = related_post
      new_comment.user = current_user
    
      new_comment.save()
      
      return Response(request.data)
    except Exception  as error:
      print(error)
      return Response("something sent wrong again")
    
class CommentByIdView(APIView): 
  def get(self, request, commentId: int): 
    try: 
      currentComment = CommentModel.objects.select_related("post").get(id = commentId)

      serialized_comment = CommentSerializer(currentComment)
      
      return Response(serialized_comment.data)
      
    except: return Response("no comment found") 
     
  def delete(self, request, commentId: int): 
    try: 
      deleting_comment = CommentModel.objects.get(id=commentId)
      deleting_comment.delete()
      
      serialized_comment = CommentSerializer(deleting_comment)
      
      return Response(serialized_comment.data)
    except: return Response("can't be deleted")
  
  def put(self, request, commentId: int): 
    try: 
      updatingPost = CommentModel.objects.filter(id = commentId).update(**request.data)
      
      return Response(updatingPost)
    except: return Response("Can't update comment")