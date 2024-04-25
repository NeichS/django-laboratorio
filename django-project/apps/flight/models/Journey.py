from django.db import models
from apps.airport_city.models.Airport import Airport
from .Plain import Plain
from .Route import Route

class Journey(models.Model):
    id_route =  models.ForeingKey(Route, on_delete=models.CASCADE)
    airport_departure =  models.ForeignKey(Airport, on_delete=models.CASCADE)
    airport_arrival =  models.ForeignKey(Airport, on_delete=models.CASCADE)
    fk_plain = models.models.ForeignKey(Plain, on_delete=models.CASCADE)