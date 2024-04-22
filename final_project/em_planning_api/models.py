from django.db import models

# Create your models here.


class LearningPath(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    progress = models.TimeField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class EMData (models.Model):
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
