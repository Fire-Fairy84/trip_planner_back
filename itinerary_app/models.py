from django.db import models
from destination_app.models import Destination  # Asegúrate de importar el modelo Destination


class Itinerary(models.Model):
    objects = None
    DURATION_CHOICES = [
        (1, '1 Day'),
        (2, '2 Days'),
        (3, '3 Days'),
    ]

    description = models.TextField()  # Descripción del itinerario
    duration = models.IntegerField(choices=DURATION_CHOICES)  # Duración del itinerario en días (1, 2 o 3 días)
    destination = models.ForeignKey(Destination, related_name='itineraries',
                                    on_delete=models.CASCADE)  # Relación con el destino
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.destination.name} ({self.duration} days)"

    class Meta:
        unique_together = (
            'destination', 'duration')  # Para evitar itinerarios duplicados con el mismo nombre para un destino
