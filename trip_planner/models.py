from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)


def __str__(self):
    return f'User: {self.name}'
