# Generated by Django 4.0.3 on 2022-03-10 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_user_image_delete_profileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
