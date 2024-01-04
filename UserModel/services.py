from django.http import JsonResponse
from .Models import UserModel
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def FindOne(id):
    try:
        user = UserModel.objects.get(pk=int(id))    
        return user
    except UserModel.DoesNotExist:
        return None
    
def FindOneAndSerialize(id):
    try:
        user = FindOne(id)
        if(user == None):
            return None
        serializer = UserSerializer(user)
        return serializer
    except UserModel.DoesNotExist:
        return  Response('Serialize fail !')
