# Generated by Django 3.1.7 on 2022-04-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0026_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='amount'),
        ),
    ]