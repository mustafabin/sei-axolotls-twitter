from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=4)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(models.Model):
  user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
  content = models.CharField(max_length=140)
  
  def __str__(self):
    return self.content
  
class Comment(models.Model):
  user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
  content = models.CharField(max_length=140)
  post= models.ForeignKey(Post, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.content