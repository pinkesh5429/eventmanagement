# Generated by Django 4.0.3 on 2022-03-11 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]
