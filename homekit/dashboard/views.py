from django.shortcuts import render
from .models import *
from django.views.generic.base import View
from django.views.generic.detail import DetailView

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

def get_data(request, pk):
    place = Place.objects.get(pk=pk)
    context['place'] = place
    return render(request, 'dashboard/test.html', context)

class PlaceDetailView(View):
    def get(self, request, pk):
        place = Place.objects.get(pk=pk)
        temperature = Temperature.objects.filter(room__pk=pk).first()
        humidity = Humidity.objects.filter(room__pk=pk).first()
        pressure = Pressure.objects.filter(room__pk=pk).first()

        context = {
            'place': place,
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
        }

        return render(request, 'dashboard/index.html', context)

#TODO
class PlaceTestView(DetailView):
    model = Place
    def get(self, request, slug):
        place = Place.objects.get(slug=slug)
        context = {
            'place': place,
        }

        return render(request, 'test/index.html', context)