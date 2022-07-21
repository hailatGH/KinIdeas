from rest_framework.routers import DefaultRouter

from company_profile.views import CompanyProfileViewSet
from music.views import ArtistViewSet, AlbumViewSet, GenreViewSet, \
    TrackViewSet, LyricsViewSet, MusicPlayerAPIView
from podcast.views import HostViewSet, SeasonViewSet, \
    PodcastCategoryViewSet, EpisodeViewSet
from radio.views import RadioViewSet

router = DefaultRouter()

# Company URLs
router.register(r'profile', CompanyProfileViewSet, basename="profile")

# Music URLs
router.register(r'artist', ArtistViewSet, basename="artist")
router.register(r'album', AlbumViewSet, basename="album")
router.register(r'genre', GenreViewSet, basename="genre")
router.register(r'track', TrackViewSet, basename="track")
router.register(r'lyrics', LyricsViewSet, basename="lyrics")
router.register(r'musicplayer', MusicPlayerAPIView, basename="musicplayer")

# Podcast
router.register(r'host', HostViewSet, basename="host")
router.register(r'season', SeasonViewSet, basename="season")
router.register(r'podcast_category', PodcastCategoryViewSet, basename="podcast_category")
router.register(r'episode', EpisodeViewSet, basename="episode")

# Radio
router.register(r'radio', RadioViewSet, basename="radio")