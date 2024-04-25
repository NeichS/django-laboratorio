from django.db import models

class Route(models.Model):
    id_flight = models.ForeignKey(models.Flight, on_delete=models.CASCADE)
    
