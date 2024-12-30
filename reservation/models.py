from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='room_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Image for {self.room.name}"

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkIn = models.DateField()
    checkOut = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Complete', 'Complete')])
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add this line

    def __str__(self):
        return f"{self.guest.name} - {self.room.name}"

class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment for {self.reservation}"

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='facility_images/')

    def __str__(self):
        return self.name

