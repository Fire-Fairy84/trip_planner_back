from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ItinerarySerializer
from .models import Itinerary


# Create your views here.
class ItineraryView(viewsets.ModelViewSet):
    serializer_class = ItinerarySerializer

    # Usar modelo a través del ORM
    queryset = Itinerary.objects.all()
