from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AccommodationSerializer
from .models import Accommodation


# Create your views here.
class AccommodationView(viewsets.ModelViewSet):
	serializer_class = AccommodationSerializer

	# Usar modelo a través del ORM
	queryset = Accommodation.objects.all()
