from django.db import models
from django.utils.translation import gettext_lazy as _
from core import validators
from core.settings import MEDIA_ROOT

def radio_cover_images(instance, filename):
    return '/'.join(['radio_cover_images', str(instance.station_name), filename])
    # The directory arrangment will be [Media/radio_cover_images/{station_name}/{filename}]

class Radio(models.Model):
    
    class Meta:
        verbose_name = _("Radio")
        verbose_name_plural = _("Radios")
        ordering = ['id']

    station_name = models.CharField(max_length=100, default='Unknown_radio', null=False, blank= False)
    station_frequency = models.FloatField(default=0, null=False, blank=False)
    station_url = models.CharField(max_length=1023, default = "", null=False , blank= False)
    station_cover = models.FileField(upload_to=radio_cover_images, validators=[validators.validate_image_extension], null=False, blank=False)
    station_description = models.TextField(blank=True, null=True, max_length=1023)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.station_name)