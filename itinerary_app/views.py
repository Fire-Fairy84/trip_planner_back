from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ItinerarySerializer, ItineraryDetailsSerializer
from .models import Itinerary, ItineraryDetails


# Create your views here.
class ItineraryView(viewsets.ModelViewSet):
    serializer_class = ItinerarySerializer

    # Usar modelo a través del ORM
    queryset = Itinerary.objects.all()


class ItineraryDetailsView(viewsets.ModelViewSet):
    serializer_class = ItineraryDetailsSerializer
    queryset = ItineraryDetails.objects.all()
