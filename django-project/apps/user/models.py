from django.db import models
from apps.pasaje import models
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(unique=True, max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.nombre + " " + self.apellido
    

class Intinerario(models.Model):
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_pasaje = models.ForeignKey(models.Pasaje, on_delete=models.CASCADE) 