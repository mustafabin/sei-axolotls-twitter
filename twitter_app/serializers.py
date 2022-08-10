from rest_framework import serializers
from .models import User_profile
class User_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = '__all__'

