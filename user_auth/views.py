from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.

class SignupView(APIView):
  def get(self,request):
    result = User.objects.all()
    all_users = UserSerializer(result,many=True)
    return Response(all_users.data)
  def post(self,request):
    data = self.request.data
    username = data["username"]
    password = data["password"]
    re_password = data["re_password"]
    # {
    #   "username":"newMustafa",
    #   "password":"123",
    #   "re_password":"123"
    # }
    try:
        if password == re_password:
            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists"})
            else:
              user = User.objects.create_user(
                  username=username, password=password)

              return Response({
                "success": "User created successfully",
    
                                })
        else:
            return Response({"error": "Passwords do not match"})
    except:
        return Response({"error": "Something went wrong signing up"})