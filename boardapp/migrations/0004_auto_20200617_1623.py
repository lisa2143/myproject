# Generated by Django 3.0.6 on 2020-06-17 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='posted_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
    ]
