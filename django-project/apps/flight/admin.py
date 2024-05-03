from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Flight)
admin.site.register(FlightHistory)
admin.site.register(Itinerary)
admin.site.register(Plane)
admin.site.register(Ticket)