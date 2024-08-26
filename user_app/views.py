from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User


# Create your views here.
class UserView(viewsets.ModelViewSet):
	serializer_class = UserSerializer

	# Usar modelo a través del ORM
	queryset = User.objects.all()


