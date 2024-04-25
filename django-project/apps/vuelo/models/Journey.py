from django.db import models


class Trayecto(models.Model):
    id_route =  models.ForeingKey(models.Route, on_delete=models.CASCADE)
    airport_departure =  models.ForeignKey(models.Airport, on_delete=models.CASCADE)
    airport_arrival =  models.ForeignKey(models.Airport, on_delete=models.CASCADE)
    fk_plain = models.models.ForeignKey(models.Plain, on_delete=models.CASCADE)