from django.contrib import admin

from .models import Favourite, Playlist

# Register your models here.

admin.site.register(Favourite)
admin.site.register(Playlist)