from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    edad   = models.IntegerField(default=0)