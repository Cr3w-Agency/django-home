from django.urls import path
from .views import *

urlpatterns = [
    path('temperature/', TemperatureListView.as_view()),
    path('temperature/last/', TemperatureLastView.as_view()),
]