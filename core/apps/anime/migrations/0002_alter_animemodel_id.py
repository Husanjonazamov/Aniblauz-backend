# Generated by Django 5.1.3 on 2025-02-17 14:19

import core.apps.anime.models.anime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animemodel',
            name='id',
            field=models.CharField(default=core.apps.anime.models.anime.generate_random_id, editable=False, max_length=500, primary_key=True, serialize=False),
        ),
    ]
