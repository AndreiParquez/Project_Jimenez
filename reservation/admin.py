from django.contrib import admin
from .models import Guest,RoomImage, Room, Reservation, Payment, Facility

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]

admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Facility)
admin.site.register(RoomImage)
