# Generated by Django 4.0.6 on 2022-07-22 13:34

import core.validators
from django.db import migrations, models
import django.db.models.deletion
import player.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(default='Unknown Album', max_length=100)),
                ('album_cover', models.ImageField(upload_to=player.models.Albums_Profile_Images, validators=[core.validators.validate_image_extension])),
                ('album_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('user_id', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(default='Unknown Artist', max_length=100)),
                ('artist_title', models.CharField(default='Unknown', max_length=100)),
                ('artist_cover', models.ImageField(upload_to=player.models.Artists_Profile_Images, validators=[core.validators.validate_image_extension])),
                ('artist_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('user_id', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_title', models.CharField(default='Unknown Genre', max_length=100)),
                ('genre_cover', models.ImageField(upload_to=player.models.Genres_Cover_Images, validators=[core.validators.validate_image_extension])),
                ('genre_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('user_id', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(default='Unknown Track', max_length=100)),
                ('track_description', models.TextField(blank=True, max_length=1023, null=True)),
                ('track_file', models.FileField(upload_to=player.models.Track_Files, validators=[core.validators.validate_track_extension])),
                ('track_status', models.BooleanField(default=False)),
                ('track_release_date', models.DateTimeField()),
                ('user_id', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks_al', to='player.album')),
                ('artist_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks_ar', to='player.artist')),
                ('genre_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks_g', to='player.genre')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrics_title', models.CharField(default='Unknown Lyrics', max_length=100)),
                ('lyrics_detail', models.TextField()),
                ('user_id', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('track_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lyrics', to='player.track')),
            ],
            options={
                'verbose_name': 'Lyrics',
                'verbose_name_plural': 'Lyrics',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='albums', to='player.artist'),
        ),
    ]