from django.db import models 

class Flight(models.Model):
    code = models.CharField(max_length=10,unique=True)
    stopover = bool
    departure_time = models.datafield()
    route = models.ForeignKey(models.Route, on_delete=models.CASCADE)
    airport_departure = models.ForeignKey(models.Airport, on_delete=models.CASCADE)
    airport_arrival = models.ForeignKey(models.Airport, on_delete=models.CASCADE)
    
    def __str__(self):
        stopover = "Tiene escala" if(self.stopover) else "No tiene escala"
        return f"Codigo: {self.code}, hora: {self.departure_time}, {stopover}"
