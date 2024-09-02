from rest_framework import serializers
from accommodation_app.models import Accommodation


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation

        fields = '__all__'
