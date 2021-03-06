# Generated by Django 3.1.7 on 2022-04-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0027_event_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='checksum',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='made_by',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='made_on',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='order_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='aemail',
            field=models.EmailField(default='aemail', max_length=100, verbose_name='aemail'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='aname',
            field=models.CharField(default='aname', max_length=120, verbose_name='aname'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='aphone',
            field=models.CharField(default='aphone', max_length=10, verbose_name='aphone'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='eid',
            field=models.IntegerField(default=0, verbose_name='eid'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ename',
            field=models.CharField(default='ename', max_length=120, verbose_name='ename'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='oid',
            field=models.CharField(default='oid', max_length=120, verbose_name='oid'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='tamount',
            field=models.IntegerField(default=0, verbose_name='tamount'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='tdate',
            field=models.CharField(default='tdate', max_length=120, verbose_name='tdate'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='tid',
            field=models.CharField(default='tid', max_length=120, verbose_name='tid'),
        ),
    ]
