from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_name = models.CharField(max_length=255,null=True,blank=True)
    operating_air_line = models.CharField(max_length=255,null=True,blank=True)
    departure_city = models.CharField(max_length=255,null=True,blank=True)
    arrival_city = models.CharField(max_length=255,null=True,blank=True)
    deate_departure = models.DateField()
    estimated_departure_time = models.TimeField()

class Passanger(models.Model):
    first_name =  models.CharField(max_length=255,null=True,blank=True)
    last_name =  models.CharField(max_length=255,null=True,blank=True)
    email =  models.CharField(max_length=255,null=True,blank=True)
    phone =  models.CharField(max_length=255,null=True,blank=True)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passanger = models.OneToOneField(Passanger,on_delete=models.CASCADE)
