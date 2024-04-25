from django.db import models
from .Flight import Flight

class Route(models.Model):
    id_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
