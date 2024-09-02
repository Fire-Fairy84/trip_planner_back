from rest_framework import serializers
from itinerary_app.models import Itinerary, ItineraryDetails, Favorites


# Serializamos la data que trae ese objeto, en este caso el objeto User
class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'


class ItineraryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryDetails
        fields = '__all__'


class ItinerarySerializer(serializers.ModelSerializer):
    details = ItineraryDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        # Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí
        # le decimos que queremos que serialice todos los campos
        fields = '__all__'

