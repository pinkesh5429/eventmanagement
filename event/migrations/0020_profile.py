# Generated by Django 4.0.3 on 2022-03-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_remove_user_password1_remove_user_password2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Id')),
                ('genders', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
    ]
