from django.contrib import admin
from .models import Guest, Room, Reservation, Payment, Facility

admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Facility)
