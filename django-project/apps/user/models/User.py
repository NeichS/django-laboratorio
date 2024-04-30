from django.db import models


class User (models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length= 100)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

