from django.db import models
from apps.aeropuerto_ciudad import models

# Create your models here.
class Vuelo(models.Model):
    codigo = models.CharField(max_length=10,unique=True)
    escala = bool
    hora = models.datafield()
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    aeropuertoSalida = models.ForeignKey(models.Aeropuerto, on_delete=models.CASCADE)
    aeropuertoDestino = models.ForeignKey(models.Aeropuerto, on_delete=models.CASCADE)

