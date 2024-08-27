from rest_framework import serializers
from itinerary_app.models import Itinerary


# Serializamos la data que trae ese objeto, en este caso el objeto User
class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        # Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí
        # le decimos que queremos que serialice todos los campos
        fields = '__all__'