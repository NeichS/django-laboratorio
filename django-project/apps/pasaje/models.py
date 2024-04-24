from django.db import models
from apps.user import models
from apps.vuelo import models

# Create your models here. (TABLAS = PASAJE, ASIENTO)

class Pasaje(models.Model):
    fecha = models.DateField()
    clase = models.CharField(max_length=20)
    fk_usuario = models.ForeignKey(models.Usuario, on_delete=models.CASCADE)
    fk_vuelo = models.ForeignKey(models.Vuelo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Fecha: {self.fecha}, Clase: {self.clase}" 
    
    
    
class asiento(models.Model):
    ubicaion = models.CharField(max_length=4)
    fk_pasaje = models.ForeignKey(Pasaje, on_delate =models.CASCADE)    
    
    def __str__(self):
        return f"Ubicacion: {self.ubicaion}"
                         