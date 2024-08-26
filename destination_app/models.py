from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Nombre del destino
    description = models.TextField()  # Descripción del destino
    country = models.CharField(max_length=100)  # País donde se encuentra el destino
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)  # Imagen opcional del destino


    def __str__(self):
        return f'Destino: {self.name}, País: {self.country}'
