from django.db import models


# Create your models here.

class User(models.Model):
    objects = None
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    user_name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return f'Usuario: {self.user_name}, Nombre: {self.name}'
