# Generated by Django 3.1.1 on 2020-09-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGroupDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agegrp', models.CharField(max_length=20)),
                ('totalcases', models.IntegerField(default=0)),
                ('percentage', models.CharField(max_length=10)),
            ],
        ),
    ]
