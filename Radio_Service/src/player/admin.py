from django.contrib import admin

from .models import RadioStation, RadioStationFavourites

# Register your models here.

admin.site.register(RadioStation)
admin.site.register(RadioStationFavourites)