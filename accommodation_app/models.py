from django.db import models
from destination_app.models import Destination


class Accommodation(models.Model):
    TYPE_CHOICES = [
        ('hotel', 'Hotel'),
        ('hostel', 'Hostel'),
        ('apartment', 'Apartment'),
        ('bnb', 'Bed and Breakfast'),
        ('camping', 'Camping'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=100, null=True, blank=True)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.ForeignKey(Destination, related_name='accommodations', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='utils/img/accommodations/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}- {self.type}in {self.destination.name}"
