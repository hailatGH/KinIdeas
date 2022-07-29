from django.contrib import admin

from .models import MusicArtist, MusicAlbum, MusicTrack, MusicGenre, MusicLyrics, MusicPlayList, MusicPlayListTracks, MusicFavourites

# Register your models here.

admin.site.register(MusicArtist)
admin.site.register(MusicAlbum)
admin.site.register(MusicGenre)
admin.site.register(MusicTrack)
admin.site.register(MusicLyrics)
admin.site.register(MusicPlayList)
admin.site.register(MusicPlayListTracks)
admin.site.register(MusicFavourites)