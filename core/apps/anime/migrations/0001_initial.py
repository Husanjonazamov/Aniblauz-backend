# Generated by Django 5.1.3 on 2025-03-05 07:59

import core.apps.anime.models.anime
import core.apps.anime.models.episode
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=core.apps.anime.models.anime.generate_random_id, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('anime_id', models.CharField(max_length=255, verbose_name='anime')),
            ],
            options={
                'verbose_name': 'Animelar',
                'verbose_name_plural': 'Animelar',
                'db_table': 'anime',
            },
        ),
        migrations.CreateModel(
            name='EpisodeModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=core.apps.anime.models.episode.generate_random_id, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('episode_id', models.CharField(max_length=255, verbose_name='episode')),
                ('link', models.URLField(blank=True, max_length=500, null=True, verbose_name='link')),
                ('anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='anime.animemodel')),
            ],
            options={
                'verbose_name': 'Anime qismlari',
                'verbose_name_plural': 'Anime qismlari',
                'db_table': 'episode',
            },
        ),
    ]
