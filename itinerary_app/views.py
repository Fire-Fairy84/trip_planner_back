from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ItinerarySerializer, ItineraryDetailsSerializer, FavoritesSerializer
from .models import Itinerary, ItineraryDetails, Favorites


class ItineraryView(viewsets.ModelViewSet):
    serializer_class = ItinerarySerializer

    queryset = Itinerary.objects.all()


class ItineraryDetailsView(viewsets.ModelViewSet):
    serializer_class = ItineraryDetailsSerializer
    queryset = ItineraryDetails.objects.all()


class FavoritesView(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()
