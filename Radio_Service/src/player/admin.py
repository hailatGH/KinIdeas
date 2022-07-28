from django.contrib import admin

from .models import Station, Favourites

# Register your models here.

admin.site.register(Station)
admin.site.register(Favourites)