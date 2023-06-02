from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    mark = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)
    # parking_spot = models.ForeignKey('ParkingSpot', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.mark} {self.model} ({self.license_plate})"


class ParkingSpot(models.Model):
    number = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(1000)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_busy = models.BooleanField(default=False)
    cars = models.ManyToManyField(Car, help_text="Select a car for this parking")

    def __str__(self):
        return f"Parking Spot {self.number}"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class Account(models.Model): # счет в банке, для возможности оплаты
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='accounts')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)