from rest_framework import serializers
from django.contrib.auth.models import User


# Serializamos la data que trae ese objeto, en este caso el objeto User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí
        # le decimos que queremos que serialice todos los campos
        fields = '__all__'
