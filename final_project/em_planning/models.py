from django.db import models
from django_matplotlib.fields import MatplotlibFigureField

# Create your models here.


class EMData(models.Model):
    Date = models.DateField(("date"), auto_now=True)
    Time = models.DateTimeField(("time"), auto_now=True)
    Frequency = models.IntegerField("frequency")
    Device = models.CharField(("device"), max_length=255)
    Location = models.CharField(("location"), max_length=255)
    Grid_1 = models.IntegerField("grid_1")
    Grid_2 = models.IntegerField("grid_2")
    Lat = models.IntegerField("lat")
    Long = models.IntegerField("long")
    NearHit = models.BooleanField("nearhit")


class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class MyModelWithFigure(models.Model):
    # ... other fields
    # figures.py should be in the same directory where models.py is placed.
    # see  ./django_matplotlib/figures.py for example.
    fig = MatplotlibFigureField(figure='test_figure', verbose_name='figure',
                                silent=True)
    # ... other fields
