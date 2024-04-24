from django.db import models


# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10,unique=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)