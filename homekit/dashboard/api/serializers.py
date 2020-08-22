from rest_framework import serializers
from ..models import *


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('value', 'room')


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ('value',)

class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = ('value',)

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name',)

