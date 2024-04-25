from django.db import models
from .City import City

class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10,unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Aeropuerto: {self.name}, Codigo: {self.code}, Ciudad: {self.city}"