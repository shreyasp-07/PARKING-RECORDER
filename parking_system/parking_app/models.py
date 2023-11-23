from django.db import models

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='parking_images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_number
