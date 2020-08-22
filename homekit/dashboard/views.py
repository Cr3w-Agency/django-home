from django.shortcuts import render
from .models import *

def get_main(request):
    return render(request, 'dashboard/home.html')

def get_values(request):
    temperature = Temperature.objects.first()
    humidity = Humidity.objects.first()
    pressure = Pressure.objects.first()
    context = {
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
    }
    return render(request, 'dashboard/index.html', context)
