from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
#imports for funtion based views, decorators access
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'NewDevice': '/create-device/',
        'AllDevice': '/all-device/',
        'AllDeviceHistory': '/all-device-history/',
        'DeviceHistory': '/device-history/',
        'UpdateDeviceStatus': '/update-device-status/<int:id>/',
        'DeleteDevice': '/delete-device/<int:id>/'
    }
    return Response(api_urls)

@api_view(['POST'])
def newDevice(request):
    serializer = DeviceSerializer(data =request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def allDevices(request):
    data = Device.objects.all()
    serializer =DeviceSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def updateDeviceHistory(request):
    serializer = ActionSerializer(data =request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def allDeviceHistory(request):
    data = LogAction.objects.all()
    serializer =ActionSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deviceHistory(request,id):
    data = LogAction.objects.filter(device_id=id)
    serializer =ActionSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteDevice(request, id):
    data = Device.objects.get(id=id)
    data.delete()
    return Response('Device Deleted')
