from rest_framework import serializers
from .models import User_profile, Comment, Post
class User_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = '__all__'

class Comment_Serializer(serializers.ModelSerializer):
  class Meta:
      model = Comment
      fields = '__all__'
      
class Post_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'