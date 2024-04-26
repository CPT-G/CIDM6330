# from django.db import models

# # Create your models here.


# class EMData(models.Model):
#     Date = models.DateField(("date"), auto_now=True)
#     Time = models.DateTimeField(("time"), auto_now=True)
#     Frequency = models.IntegerField("frequency")
#     Device = models.CharField(("device"), max_length=6)
#     Location = models.CharField(("location"), max_length=5)
#     Grid_1 = models.IntegerField("grid_1")
#     Grid_2 = models.IntegerField("grid_2")
#     Lat = models.IntegerField("lat")
#     Long = models.IntegerField("long")
#     NearHit = models.BooleanField("nearhit")

#     def __str__(self):
#         return self.Date

from django.db import models
# from django_matplotlib.fields import MatplotlibFigureField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Customer(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('I', 'Intersex')
    )

    title = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    created_by = models.ForeignKey(
        User, related_name='created_by', on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

    # Customer.objects.filter(status='published')
    # Customer.published.all()


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


# class MyModelWithFigure(models.Model):
#     # ... other fields
#     # figures.py should be in the same directory where models.py is placed.
#     # see  ./django_matplotlib/figures.py for example.
#     fig = MatplotlibFigureField(figure='test_figure', verbose_name='figure',
#                                 silent=True)
#     # ... other fields
