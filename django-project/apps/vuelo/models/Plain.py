from django.db import models

class Avion(models.Model):
    SIZE_CHOICES = [
        ('simple', 'Simple'),
        ('medium', 'Medium'),
        ('full', 'Full'),
    ]
    
    plain_model_name = models.CharField(max_lenght=50)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    