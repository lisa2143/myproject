# Generated by Django 3.0.6 on 2020-07-19 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0008_auto_20200711_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
