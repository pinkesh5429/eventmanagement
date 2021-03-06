# Generated by Django 3.1.7 on 2022-03-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0020_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='username',
            field=models.TextField(null=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
