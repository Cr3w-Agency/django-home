from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_main),
    path('home/<int:pk>/', PlaceListView.as_view(), name='place_view'),
]

