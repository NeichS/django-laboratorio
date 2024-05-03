from django.contrib import admin

from .models.Airport import Airport
from .models.City import City
# Register your models here.

admin.site.register(Airport)
admin.site.register(City)