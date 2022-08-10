from rest_framework import viewsets
from .models import User_profile
from .serializers import User_profileSerializer
# Create your views here.

class UserProfile_ViewSet(viewsets.ModelViewSet):
  queryset = User_profile.objects.all()
  serializer_class = User_profileSerializer;