from django.contrib import admin

from .models import PodcastHost, PodcastSeason, PodcastEpisode, PodcastCategory, PodcastPlayList, PodcastPlayListEpisodes, PodcastFavourites

# Register your models here.

admin.site.register(PodcastHost)
admin.site.register(PodcastSeason)
admin.site.register(PodcastEpisode)
admin.site.register(PodcastCategory)
admin.site.register(PodcastPlayList)
admin.site.register(PodcastPlayListEpisodes)
admin.site.register(PodcastFavourites)