from rest_framework import serializers
from .models import *


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAction
        fields = '__all__'
