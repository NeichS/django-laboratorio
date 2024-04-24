from django.db import models


# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"Ciudad: {self.nombre}"

class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10,unique=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Aeropuerto: {self.nombre}, Codigo: {self.codigo}, Ciudad: {self.ciudad}"