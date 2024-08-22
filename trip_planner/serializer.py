from rest_framework import serializers
from trip_planner.models import User

# Serializamos la data que trae ese objeto, en este caso el objeto Person
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		# Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí le decimos que queremos que serialice todos los campos
		fields = '__all__'