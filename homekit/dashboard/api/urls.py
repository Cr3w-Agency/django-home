from django.urls import path
from .views import *

urlpatterns = [
    path('temperature/', TemperatureView.as_view()),
    path('pressure/', PressureView.as_view()),
    path('humidity/', HumidityView.as_view())
]