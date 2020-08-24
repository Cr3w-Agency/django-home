from rest_framework import serializers
from ..models import *


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('value', 'room')

    def create(self, validated_data):
        return Temperature.objects.create(**validated_data)


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ('value', 'room')

class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = ('value', 'room')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name',)

