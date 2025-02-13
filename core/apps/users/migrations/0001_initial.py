# Generated by Django 5.1.3 on 2025-02-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('user_id', models.CharField(max_length=50, verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'UserModel',
                'verbose_name_plural': 'UserModels',
                'db_table': 'user',
            },
        ),
    ]
