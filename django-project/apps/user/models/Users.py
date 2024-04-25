from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dni = models.CharField(unique=True, max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name + " " + self.lastname
    