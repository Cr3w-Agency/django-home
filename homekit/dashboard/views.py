from django.shortcuts import render
from .models import *
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic import ListView


def get_main(request):
    place = Place.objects.first()
    context = {
        'direct_url': place
    }
    return render(request, 'dashboard/home.html', context)

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

#WORKCABLE
class PlaceDetailView(View):
    def get(self, request, place_id):
        place = Place.objects.get(pk=place_id)
        temperature = Temperature.objects.filter(room__pk=place_id).first()
        humidity = Humidity.objects.filter(room__pk=place_id).first()
        pressure = Pressure.objects.filter(room__pk=place_id).first()

        context = {
            'place': place,
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
        }

        return render(request, 'dashboard/index.html', context)

#TODO
class PlaceListView(ListView):
    model = Place
    template_name = 'dashboard/index.html'
    context_object_name = 'place'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['temperature'] = Temperature.objects.filter(room__pk=self.kwargs['pk']).first()
        context['humidity'] = Humidity.objects.filter(room__pk=self.kwargs['pk']).first()
        context['pressure'] = Pressure.objects.filter(room__pk=self.kwargs['pk']).first()
        return context

    def get_queryset(self):
        return Place.objects.get(pk=self.kwargs['pk'])