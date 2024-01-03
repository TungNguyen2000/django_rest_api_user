from django.http import JsonResponse
from .Models import UserModel
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def Create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET'])
def FindAll(request)
    users = UserModel.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FindOne(request,id)
    user = FindOneAndSerialize(id)
    if(user == null):
        return  Response(status=status.HTTP_404_NOT_FOUND)
    return Response(user)
    
@api_view(['PUT'])
def Update(request,id)
       user = FindOne(id)
        if(user == null):
            return  Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def Delete(request, id):
        user = FindOne(id)
        if(user == null):
            return  Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
 
       


 
 