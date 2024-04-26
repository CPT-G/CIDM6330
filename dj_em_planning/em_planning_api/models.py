from django.db import models

# Create your models here.


class EMData(models.Model):
    Date = models.DateField(("date"), auto_now=True)
    Time = models.DateTimeField(("time"), auto_now=True)
    Frequency = models.IntegerField("frequency")
    Device = models.CharField(("device"), max_length=6)
    Location = models.CharField(("location"), max_length=5)
    Grid_1 = models.IntegerField("grid_1")
    Grid_2 = models.IntegerField("grid_2")
    Lat = models.IntegerField("lat")
    Long = models.IntegerField("long")
    NearHit = models.BooleanField("nearhit")

    def __str__(self):
        return self.Date
