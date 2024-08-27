from rest_framework import serializers
from accommodation_app.models import Accommodation


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        # Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí
        # le decimos que queremos que serialice todos los campos
        fields = '__all__'
