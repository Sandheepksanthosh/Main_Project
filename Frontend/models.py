from django.db import models

# Create your models here.
class Makeatripdb(models.Model):
    pickup_location = models.CharField(max_length=100, null=True, blank=True)
    dropoff_location = models.CharField(max_length=100, null=True, blank=True)
    picup_date = models.DateField(null=True, blank=True)
    dropoff_date = models.DateField(null=True, blank=True)
    pickup_time = models.IntegerField(null=True, blank=True)
