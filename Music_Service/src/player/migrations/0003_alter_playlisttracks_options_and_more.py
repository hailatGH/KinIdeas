# Generated by Django 4.0.6 on 2022-07-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_remove_playlist_track_id_playlisttracks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlisttracks',
            options={'ordering': ['id'], 'verbose_name': 'PlayListTrack', 'verbose_name_plural': 'PlayListTracks'},
        ),
        migrations.AddField(
            model_name='playlist',
            name='playlist_description',
            field=models.TextField(blank=True, max_length=1023, null=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='playlist_name',
            field=models.CharField(default='Unknown Track', max_length=100),
        ),
    ]