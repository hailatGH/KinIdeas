from django.contrib import admin

from .models import Host, Season, Episode, PodcastCategory

# Register your models here.

admin.site.register(Host)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(PodcastCategory)