from django.db import models
from destination_app.models import Destination


class Activity(models.Model):
    TYPE_CHOICES = [
        ('adventure', 'Adventure'),
        ('cultural', 'Cultural'),
        ('nature', 'Nature'),
        ('gastronomic', 'Gastronomic'),
        ('historical', 'Historical'),
        ('relaxation', 'Relaxation'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    destination = models.ForeignKey(Destination, related_name='activities', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='utils/img/activities/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.type} at {self.destination.name}"
