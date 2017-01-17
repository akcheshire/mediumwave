from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Station(models.Model):
    freq = models.IntegerField()
    station_name = models.CharField(max_length=64)
    transmitter = models.CharField(max_length=64)
    power = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField(blank=True)
    
    def publish(self):
        self.save()
    
    def __str__(self):
        return str(self.freq) + ": " + self.station_name + " - " + self.transmitter + " (" + str(self.power) + "kW)"
