from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from knox.models import AuthToken
from twitter_app.models import User_profile
from twitter_app.serializers import User_profileSerializer
# Create your views here.

class SignupView(APIView):
  permission_classes = [
    permissions.AllowAny
  ]

  def get(self,request):
    result = User.objects.all()
    all_users = UserSerializer(result,many=True)
    return Response(all_users.data)
  def post(self,request):
    data = self.request.data
    username = data["username"]
    email = data["email"]
    password = data["password"]
    re_password = data["re_password"]
    try:
        if password == re_password:
            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists"})
            else:
              user = User.objects.create_user(
                  username=username, password=password)
              User_profile.objects.create(user=user,email=email,name=username)
              return Response({
                "success": "User created successfully",
                "token": AuthToken.objects.create(user)[1]
                                })
        else:
            return Response({"error": "Passwords do not match"})
    except:
        return Response({"error": "Something went wrong signing up"})
      
class LoginView(APIView):
  permission_classes = [
    permissions.AllowAny
  ]

  def post(self,request):
    data = self.request.data
    username = data["username"]
    password = data["password"]
    try:
      user = auth.authenticate(username=username, password=password)
      if user is not None:
          auth.login(request, user)
          return Response({"success": "User authenticated",
                            "token": AuthToken.objects.create(user)[1]})
      else:
          return Response({"error": "Error Authenticating"})
    except:
        return Response({"error": "Something went wrong when logging in"})

class GrabProfile(APIView):
    def get(self, request):
        try:
            user = self.request.user
            profile = User_profile.objects.get(user=user)
            profile_json = User_profileSerializer(profile)
            return Response({"profile": profile_json.data})
        except:
            return Response({"error": "( ﾟДﾟ)b  no user profile found "})