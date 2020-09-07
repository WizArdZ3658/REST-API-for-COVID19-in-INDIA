# Generated by Django 3.1.1 on 2020-09-07 11:03

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
        migrations.CreateModel(
            name='Covid19India',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('StateUT', models.CharField(max_length=50)),
                ('ConfirmedIndianNational', models.CharField(max_length=10)),
                ('ConfirmedForeignNational', models.CharField(max_length=10)),
                ('Cured', models.IntegerField()),
                ('Deaths', models.IntegerField()),
                ('Confirmed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HospitalBeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StateUT', models.CharField(max_length=50)),
                ('NumPrimaryHealthCenters', models.IntegerField(default=0)),
                ('NumCommunityHealthCenters', models.IntegerField(default=0)),
                ('NumSubDistrictHospitals', models.IntegerField(default=0)),
                ('NumDistrictHospitals', models.IntegerField(default=0)),
                ('TotalPublicHealthFacilities', models.IntegerField(default=0)),
                ('NumPublicBeds', models.IntegerField(default=0)),
                ('NumRuralHospitals', models.IntegerField(default=0)),
                ('NumRuralBeds', models.IntegerField(default=0)),
                ('NumUrbanHospitals', models.IntegerField(default=0)),
                ('NumUrbanBeds', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ICMRTestingLabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
                ('City', models.CharField(max_length=200)),
                ('StateUT', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IndiaCensus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StateUT', models.CharField(max_length=50)),
                ('Population', models.IntegerField()),
                ('Ruralpopulation', models.IntegerField()),
                ('Urbanpopulation', models.IntegerField()),
                ('Area', models.CharField(max_length=100)),
                ('Density', models.CharField(max_length=100)),
                ('GenderRatio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IndividualDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('government_id', models.CharField(max_length=50)),
                ('diagnosed_date', models.DateField()),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=1)),
                ('City', models.CharField(max_length=200)),
                ('detected_district', models.CharField(max_length=200)),
                ('StateUT', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('current_status', models.CharField(max_length=50)),
                ('status_change_date', models.DateField()),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('StateUT', models.CharField(max_length=50)),
                ('TotalSamples', models.IntegerField(default=0)),
                ('Negative', models.IntegerField(default=0)),
                ('Positive', models.IntegerField(default=0)),
            ],
        ),
    ]
