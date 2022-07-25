from rest_framework.routers import DefaultRouter

from player.views import ArtistViewSet, AlbumViewSet, GenreViewSet, \
    TrackViewSet, LyricsViewSet, PlayListViewSet, FavouriteListViewSet

from player.player import SingleMusicPlayer

router = DefaultRouter()

router.register(r'artist', ArtistViewSet, basename="artist")
router.register(r'album', AlbumViewSet, basename="album")
router.register(r'genre', GenreViewSet, basename="genre")
router.register(r'track', TrackViewSet, basename="track")
router.register(r'lyrics', LyricsViewSet, basename="lyrics")
router.register(r'playlist', PlayListViewSet, basename="playlist")
router.register(r'favouritelist', FavouriteListViewSet, basename="favouritelist")
router.register(r'singleplay', SingleMusicPlayer, basename="singleplay")
# router.register(r'albumplay', AlbumMusicsViewSet, basename="albumplay")
# router.register(r'playlistplay', PlaylistMusicsViewSet, basename="playlistplay")
# router.register(r'favlistplay', FavlistMusicsViewSet, basename="favlistplay")