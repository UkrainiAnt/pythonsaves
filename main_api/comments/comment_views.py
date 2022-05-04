from .comment_serializers import CommentSerializer 
from .comment_models import CommentModel
from rest_framework.views import APIView 
from rest_framework.response import Response

class CommentListView(APIView): 
  def get(self, request): 
    try: 
      allComments = CommentModel.objects.all()
      print(allComments)
      serialized_comments = CommentSerializer(allComments, many=True)
      
      return Response(serialized_comments)
    except Exception as error: 
      print(error)
      return Response("something went wrong")
    
  def post(self, request): 
    try: 
      print(request.data)
      
      return Response(request.data)
    except: return Response("something sent wrong again")