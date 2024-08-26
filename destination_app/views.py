from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DestinationSerializer
from .models import Destination


# Create your views here.
class DestinationView(viewsets.ModelViewSet):
	serializer_class = DestinationSerializer

	# Usar modelo a través del ORM
	queryset = Destination.objects.all()

