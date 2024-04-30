from django.db import models
from apps.airport_management.models import Airport

class Route(models.Model):
    fk_airport_departure = models.ForeignKey(Airport, on_delete=models.CASCADE, null= False)
    fk_airport_arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, null= False)