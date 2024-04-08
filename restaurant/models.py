from django.db import models

# Create your models here.

class booking(models.Model):

    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(6)
    BookingDate = models.DateTimeField()

class menu(models.Model):
    ID = models.AutoField(primary_key=True) 
    Tittle = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(5)

