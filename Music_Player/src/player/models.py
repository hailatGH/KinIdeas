from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Playlist(models.Model):

    class Meta:
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")
        ordering = ['id']

    playlist_title = models.CharField(max_length=100,default='Other',null=False , blank= False)
    track_id = models.IntegerField(default=0)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.playlist_title)

class Favourite(models.Model):

    class Meta:
        verbose_name = _("Favourite")
        verbose_name_plural = _("Favourites")
        ordering = ['id']

    track_id = models.IntegerField(default=0)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.track_id)