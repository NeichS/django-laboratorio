from django.db import models
from .City import City

class Airport(models.Model):
    airport_code = models.CharField(max_length=100, unique=True, null=False)
    fk_city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    