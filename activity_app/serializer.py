from rest_framework import serializers
from activity_app.models import Activity


# Serializamos la data que trae ese objeto, en este caso el objeto Destination
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        # Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí
        # le decimos que queremos que serialice todos los campos
        fields = '__all__'
