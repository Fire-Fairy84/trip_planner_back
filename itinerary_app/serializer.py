from rest_framework import serializers
from itinerary_app.models import Itinerary, ItineraryDetails, Favorites



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

        fields = '__all__'
