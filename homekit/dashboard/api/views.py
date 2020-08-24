from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class TemperatureView(APIView):
    def get(self, request):
        temperature = Temperature.objects.all()
        serializer = TemperatureSerializer(temperature, many=True)
        return Response(serializer.data)

    def post(self, request):
        temperature = TemperatureSerializer(data=request.data)
        if temperature.is_valid():
            temperature.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class HumidityView(APIView):
    def get(self, request):
        humidity = Humidity.objects.all()
        serializer = HumiditySerializer(humidity, many=True)
        return Response(serializer.data)

    def post(self, request):
        humidity = HumiditySerializer(data=request.data)
        if humidity.is_valid():
            humidity.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PressureView(APIView):
    def get(self, request):
        pressure = Pressure.objects.all()
        serializer = PressureSerializer(pressure, many=True)
        return Response(serializer.data)

    def post(self, request):
        pressure = PressureSerializer(data=request.data)
        if pressure.is_valid():
            pressure.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    """ Получение последнего значение по айди комнаты """
    # def get(self, request, room_id):
    #     temperature = Temperature.objects.filter(room__pk=room_id).first()
    #     serializer = TemperatureSerializer(temperature, many=False)
    #     return Response(serializer.data)
