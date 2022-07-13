from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Favourite(models.Model):

    class Meta:
        verbose_name = _("Favourite")
        verbose_name_plural = _("Favourites")
        ordering = ['id']

    station_id = models.IntegerField(default=0)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.station_id)