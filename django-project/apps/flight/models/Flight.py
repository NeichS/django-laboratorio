from django.db import models
from .FlightHistory import FlightHistory
from apps.route.models import Route
from apps.user.models import User

class Flight(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    stopover = models.BooleanField(default=True)
    departure_time = models.DateField()
    fk_flight_history = models.ForeignKey(FlightHistory, on_delete=models.CASCADE)
    fk_route = models.ForeignKey(Route, on_delete=models.CASCADE)

class Plane(models.Model):
    plane_model = models.CharField(max_length=50)
    SIZE = [
        ('chico', 'chico'),
        ('mediano', 'mediano'),
        ('grande', 'grande'),
    ]
    size = models.CharField(
        max_length=7,
        choices=SIZE,
        default='mediano',
    )

class FlightHistory(models.Model):
    date = models.DateField()
    fk_plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

class Itinerary():
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Ticket(models.Model):
    flight_date = models.DateField()
    ticket_class = models.CharField(max_length=50) #DEFINIR CONSTRAINT
    pourchase_date = models.DateField()
    seat_location = models.CharField(max_length=50) # DEFINIR BIEN 
    fk_itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
