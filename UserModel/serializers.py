from rest_framework import serializers
from .Models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'name', 'password', 'email']