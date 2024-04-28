from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from em_planning_arch.domain.model import DomainEMData
# Create your models here.


class User(models.Model):  # URL users


class EMData(models.Model):
    """
    EM Data Model
    Defines the attributes of our EM Data
    """
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    frequency = models.IntegerField()
    device = models.CharField(max_length=6)
    location = models.CharField(max_length=5)
    grid_1 = models.IntegerField()
    grid_2 = models.IntegerField()
    lat = models.IntegerField()
    long = models.IntegerField()
    nearhit = models.BooleanField()
    FREQUENCY = (
        ('fm', 'FM'),
        ('tacsat', 'TACSAT'),
        ('jcr', 'JCR'),
        ('wifi', 'WiFi'),
    )

    def __str__(self):
        return f"{self.frequency}"

    class Meta:
        app_label = "em_planning_api"


class LatLongPoints(models.Model):  # x and y points for matplotlib


class Colors(models.Model):  # Plotted Colors based on device

    # ID 4 types of device based on frequency parameters


class FrequencyDevice(models.Model):


class DataConversion(models.Model):  # CSV to JSON


class DateTime(models.Model):
    """
    A model with a DateTimeField, used to test if DateTimeField
    changes are detected properly.
    """
    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()
    naive_dt = models.DateTimeField(null=True, blank=True)


class FakePlotting(models.Model):  # Experiment with matplotlib


class Mapping(models.Model):  # Plotting on map or chart


class Layout(models.Model):
