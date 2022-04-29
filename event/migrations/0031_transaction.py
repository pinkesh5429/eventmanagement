# Generated by Django 3.1.7 on 2022-04-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0030_delete_tp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(verbose_name='eid')),
                ('ename', models.CharField(max_length=120, verbose_name='ename')),
                ('aname', models.CharField(max_length=120, verbose_name='aname')),
                ('aemail', models.EmailField(max_length=100, verbose_name='aemail')),
                ('aphone', models.CharField(max_length=10, verbose_name='aphone')),
                ('tamount', models.IntegerField(verbose_name='tamount')),
                ('oid', models.CharField(max_length=120, verbose_name='oid')),
                ('tid', models.CharField(max_length=120, verbose_name='tid')),
                ('tdate', models.CharField(max_length=120, verbose_name='tdate')),
                ('pdate', models.CharField(max_length=120, verbose_name='pdate')),
            ],
        ),
    ]
