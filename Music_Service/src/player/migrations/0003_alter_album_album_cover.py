# Generated by Django 4.0.6 on 2022-07-23 07:42

import core.validators
from django.db import migrations, models
import player.models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_playlist_favouritelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_cover',
            field=models.ImageField(blank=True, null=True, upload_to=player.models.Albums_Profile_Images, validators=[core.validators.validate_image_extension]),
        ),
    ]
