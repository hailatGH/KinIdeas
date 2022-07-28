from django.db import models
from django.utils.translation import gettext_lazy as _
from core import validators

def Station_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Station_Cover_Images', str(instance.station_name), str(instance.station_name + " - " + filename)])
    # The directory arrangment will be [media/Albums_Profile_Images/{album_title}/{filename}]

class Station(models.Model):
    
    class Meta:
        verbose_name = _("Radio")
        verbose_name_plural = _("Radios")
        ordering = ['id']

    station_name = models.CharField(max_length=100, default='Unknown Station', null=False, blank= True, unique=True)
    station_frequency = models.FloatField(default=88, null=False, blank=False)
    station_url = models.CharField(max_length=1023, default = "", null=False , blank= False)
    station_cover = models.ImageField(upload_to=Station_Cover_Images, validators=[validators.validate_image_extension], \
        height_field=None, width_field=None, null=False, blank=True, unique=True)
    station_description = models.TextField(blank=True, null=True, max_length=1023)
    user_id =  models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%d: %s' % (self.pk, self.station_name)

class Favourites(models.Model):

    class Meta:
        verbose_name = _("Favourite")
        verbose_name_plural = _("Favourites")
        ordering = ['id']
    
    station_id = models.ForeignKey(Station, default=1, related_name='favouritelist', on_delete=models.CASCADE, \
        null=False, blank=False)
    user_id =  models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return '%d: %d' % (self.pk, self.user_id)
        return f'{self.pk} {self.user_id}'