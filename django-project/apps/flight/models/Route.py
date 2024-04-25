from django.db import models
from .Journey import Journey

class Route(models.Model):
    fk_journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    
