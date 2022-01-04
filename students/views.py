from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .models import *
from django.conf import settings
from .ApiV1_0 import (ApiStudents)


def getUserIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class insertStudent(APIView):
    def post(self, request, format=None):
        data = request.data
        request.data['PubIp'] = getUserIP(request)
        returnData = ApiStudents.insertStudent(self, request.data)

        return Response(returnData, status=status.HTTP_200_OK)
        print(returnData)
        # if returnData['RS'] == "SUCCESS":
        #     return Response(returnData, status=status.HTTP_202_ACCEPTED)
        # else:
        #     return Response(returnData, status=status.HTTP_400_BAD_REQUEST)

class listStudent(APIView):
    def post(self, request, format=None):

        request.data['PubIp'] = getUserIP(request)
        returnData = ApiStudents.listStudent(self, request.data)
        # if returnData['RS'] == "SUCCESS":
        #     return Response(returnData, status=status.HTTP_202_ACCEPTED)
        # else:
        #     return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
        return Response(returnData, status=status.HTTP_200_OK)
        print(returnData)

class deleteStudent(APIView):
    def post(self, request, format=None):

        request.data['PubIp'] = getUserIP(request)
        returnData = ApiStudents.deleteStudent(self, request.data)

        return Response(returnData, status=status.HTTP_200_OK)
        print(returnData)
        # if returnData['RS'] == "SUCCESS":
        #     return Response(returnData, status=status.HTTP_202_ACCEPTED)
        # else:
        #     return Response(returnData, status=status.HTTP_400_BAD_REQUEST)