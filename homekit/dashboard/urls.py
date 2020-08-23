from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_main),
    path('home/', get_values),
    path('home/<int:pk>/', PlaceDetailView.as_view()),
    path('home/test/<slug:slug>/', PlaceTestView.as_view()),

]

