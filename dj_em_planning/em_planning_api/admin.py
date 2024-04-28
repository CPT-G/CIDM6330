from django.contrib import admin
from .models import User, EMData, LatLongPoints, Colors, FrequencyDevice, DataConversion, DateTime, FakePlotting, Mapping, Layout

# Register your models here.


admin.site.register(User)
admin.site.register(EMData)
admin.site.register(LatLongPoints)
admin.site.register(Colors)
admin.site.register(FrequencyDevice)
admin.site.register(DataConversion)
admin.site.register(DateTime)
admin.site.register(FakePlotting)
admin.site.register(Mapping)
admin.site.register(Layout)
