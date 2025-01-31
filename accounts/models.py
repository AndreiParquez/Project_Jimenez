from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Added phone_number field
    
    

    def __str__(self):
        return self.username


