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

def UpdateUser(request, id):
    user = FindOne(id)
    if(user == None):
        return  Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

def DeleteUser(id):
    user = FindOne(id)
    if(user == None):
        return  Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def CreateUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
