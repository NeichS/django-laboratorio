from django.db import models
from .FlightHistory import FlightHistory
from apps.route.models import Route

class Flight(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    stopover = models.BooleanField(null=False)
    departure_time = models.DateField()
    fk_flight_history = models.ForeignKey(FlightHistory, on_delete=models.CASCADE)
    fk_route = models.ForeignKey(Route, on_delete=models.CASCADE)





