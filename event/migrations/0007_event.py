# Generated by Django 4.0.3 on 2022-03-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_profileimage_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('venue', models.CharField(max_length=120, verbose_name='Venue')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]