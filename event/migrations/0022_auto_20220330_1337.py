# Generated by Django 3.1.7 on 2022-03-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_auto_20220330_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='username',
            field=models.CharField(max_length=120, null=True, verbose_name='username'),
        ),
    ]