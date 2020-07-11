# Generated by Django 3.0.6 on 2020-07-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0007_auto_20200705_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='target',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]