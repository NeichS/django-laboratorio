from django.db import models
from apps.ticket.models.Ticket import Ticket
from .Users import Users

class Itinerary(models.Model):
    fk_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    fk_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE) 
    

    