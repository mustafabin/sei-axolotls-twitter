from rest_framework import viewsets
from .models import User_profile, Comment, Post
from .serializers import User_profileSerializer, Comment_Serializer, Post_Serializer
# Create your views here.

class UserProfile_ViewSet(viewsets.ModelViewSet):
  queryset = User_profile.objects.all()
  serializer_class = User_profileSerializer;
  
class Comment_ViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = Comment_Serializer;

class Post_ViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = Post_Serializer;