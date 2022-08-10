from rest_framework import serializers

class UserSerializer(serializers.BaseSerializer):
  def to_representation(self,instance):
    return {
      "id":instance.id,
      "username": instance.username,
      "password": instance.password,
    }