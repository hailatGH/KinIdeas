from django.contrib import admin

from .models import Host, Season, Episode, PodcastCategory, PlayList, PlayListEpisodes, Favourites

# Register your models here.

admin.site.register(Host)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(PodcastCategory)
admin.site.register(PlayList)
admin.site.register(PlayListEpisodes)
admin.site.register(Favourites)