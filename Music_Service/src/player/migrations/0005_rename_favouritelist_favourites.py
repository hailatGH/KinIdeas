# Generated by Django 4.0.6 on 2022-07-25 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_alter_playlisttracks_playlist_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavouriteList',
            new_name='Favourites',
        ),
    ]