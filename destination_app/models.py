from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='utils/img/destinations/', null=True, blank=True)


    def __str__(self):
        return f'Destination: {self.name}, Country: {self.country}'
