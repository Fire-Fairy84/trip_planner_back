from django.db import models
from destination_app.models import Destination
from django.db import models
from django.conf import settings
from user_app.models import User


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


class ItineraryDetails(models.Model):
    objects = None
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='details')
    day = models.IntegerField(choices=[(1, 'Day 1'), (2, 'Day 2'), (3, 'Day 3')])
    accommodation = models.ForeignKey('accommodation_app.Accommodation', on_delete=models.SET_NULL, null=True,
                                      blank=True, related_name='itinerary_details')
    activity = models.ForeignKey('activity_app.Activity', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='itinerary_details')

    class Meta:
        ordering = ['itinerary', 'day']
        verbose_name = "Itinerary Detail"
        verbose_name_plural = "Itinerary Details"

    def __str__(self):
        details = []
        if self.accommodation:
            details.append(f"Accommodation: {self.accommodation.name}")
        if self.activity:
            details.append(f"Activity: {self.activity.name}")
        return f"Day {self.day}: {', '.join(details) if details else 'No details'}"


class Favorites(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='favorites')
    saved_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            'user', 'itinerary')  # Garantiza que un usuario no pueda guardar el mismo itinerario más de una vez

    def __str__(self):
        return f"{self.user} - {self.itinerary} (saved on {self.saved_date})"
