from rest_framework import serializers
from destination_app.models import Destination


# Serializamos la data que trae ese objeto, en este caso el objeto Destination
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        # Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí
        # le decimos que queremos que serialice todos los campos
        fields = '__all__'
