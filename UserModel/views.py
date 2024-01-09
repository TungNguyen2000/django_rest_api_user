from django.http import JsonResponse
from .Models import UserModel
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import *

@api_view(['GET'])
def GetAll(request):
    users = UserModel.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Create(request):
    return CreateUser(request=request)
    
@api_view(['GET'])
def GetOne(request, id):
    user = FindOneAndSerialize(id)
    if(user == None):
        return  Response(status=status.HTTP_404_NOT_FOUND)
    return Response(user.data)

@api_view(['PUT'])
def Update(request, id):
    return UpdateUser(request=request, id=id)

@api_view(['DELETE'])
def Delete(request, id):
    return DeleteUser(id)