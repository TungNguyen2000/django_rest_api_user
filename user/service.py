from django.http import JsonResponse
from .Models import UserModel
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



def FindOne(id):
    try:
        user = UserModel.objects.get(int(pk=id))    
        return user
    except UserModel.DoesNotExist:
        return null
def FindOneAndSerialize(id)
    try:
        user = FindOne(id)
        if(user == null):
            return null
        serializer = UserSerializer(data)
        return serializer
    except  ....
        return  { mess: ' Serialize fail !'}

def handlePDF(request):
    try:
        return    ["Day laf cau thu nhat","Day la cau thu2"]
    except:
        
# def FindByTopicAndDate:
#     try:
#         raw("select ....")

def translation(pdf)
    