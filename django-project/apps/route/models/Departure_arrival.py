from django.db import models
from . import Route

class Departure_arrival(models.Model):
    fk_arrival = models.ForeignKey(Route, on_delete=models.CASCADE, null= True)
    fk_departure = models.ForeignKey(Route, on_delete=models.CASCADE, null= True)