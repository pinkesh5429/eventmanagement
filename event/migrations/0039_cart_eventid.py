# Generated by Django 3.1.7 on 2022-05-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0038_remove_cart_eventid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='eventid',
            field=models.IntegerField(default=0, verbose_name='Event_Id'),
        ),
    ]
