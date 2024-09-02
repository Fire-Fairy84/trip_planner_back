from rest_framework import serializers
from activity_app.models import Activity



class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity

        fields = '__all__'
