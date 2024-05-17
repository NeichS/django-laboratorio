from django.db import models
from apps.flightHistory.models import FlightHistory
from apps.route.models import Route
from .manager import FlightManager

class Flight(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    stopover = models.BooleanField(null=False)
    departure_time = models.TimeField()
    fk_flight_history = models.ForeignKey(FlightHistory, on_delete=models.CASCADE)
    fk_route = models.ForeignKey(Route, on_delete=models.CASCADE)

    objects = FlightManager()





