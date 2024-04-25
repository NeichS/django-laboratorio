from .Ticket import Ticket
from django.db import models

class Seat(models.Model):
    location = models.CharField(max_length=4)
    fk_ticket = models.ForeignKey(Ticket, on_delate =models.CASCADE)    
    
    def __str__(self):
        return f"Ubicacion: {self.location}"
               