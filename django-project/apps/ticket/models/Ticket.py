from django.db import models
from apps.user.models import User
from apps.flight.models import Flight


class Ticket(models.Model):
    date = models.DateField()
    ticket_class = models.CharField(max_length=20)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Fecha: {self.fecha}, Clase: {self.clase}" 
    
    