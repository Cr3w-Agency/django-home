from rest_framework import generics, status
from .serializers import *

class TemperatureLastView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def get_object(self):
        return self.queryset.first()

class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureCreate(generics.CreateAPIView):
    serializer_class = TemperatureSerializer