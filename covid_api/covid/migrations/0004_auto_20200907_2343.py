# Generated by Django 3.1.1 on 2020-09-07 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_auto_20200907_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covid19india',
            name='ConfirmedForeignNational',
        ),
        migrations.RemoveField(
            model_name='covid19india',
            name='ConfirmedIndianNational',
        ),
    ]
