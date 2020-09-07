from django.db import models


# Create your models here.


class AgeGroupDetails(models.Model):
    agegrp = models.CharField(max_length=20)
    totalcases = models.IntegerField(default=0)
    percentage = models.CharField(max_length=10)  # this is a string (float val favourable)

    def __str__(self):
        return self.agegrp


class HospitalBeds(models.Model):
    StateUT = models.CharField(max_length=50)
    NumPrimaryHealthCenters = models.IntegerField(default=0)
    NumCommunityHealthCenters = models.IntegerField(default=0)
    NumSubDistrictHospitals = models.IntegerField(default=0)
    NumDistrictHospitals = models.IntegerField(default=0)
    TotalPublicHealthFacilities = models.IntegerField(default=0)
    NumPublicBeds = models.IntegerField(default=0)
    NumRuralHospitals = models.IntegerField(default=0)
    NumRuralBeds = models.IntegerField(default=0)
    NumUrbanHospitals = models.IntegerField(default=0)
    NumUrbanBeds = models.IntegerField(default=0)


class ICMRTestingLabs(models.Model):
    lab = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    City = models.CharField(max_length=200)
    StateUT = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


# there are some missing data
class IndividualDetails(models.Model):
    government_id = models.CharField(max_length=50)
    diagnosed_date = models.DateField()
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)
    City = models.CharField(max_length=200)
    detected_district = models.CharField(max_length=200)
    StateUT = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    current_status = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)


# there are some missing data
class TestingDetails(models.Model):
    Date = models.DateField()
    StateUT = models.CharField(max_length=50)
    TotalSamples = models.IntegerField(default=0)
    Negative = models.IntegerField(default=0)
    Positive = models.IntegerField(default=0)


# there are some missing data
class Covid19India(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    StateUT = models.CharField(max_length=50)
    Cured = models.IntegerField()
    Deaths = models.IntegerField()
    Confirmed = models.IntegerField()


class IndiaCensus(models.Model):
    StateUT = models.CharField(max_length=50)
    Population = models.IntegerField()
    Ruralpopulation = models.IntegerField()
    Urbanpopulation = models.IntegerField()
    Area = models.CharField(max_length=100)
    Density = models.CharField(max_length=100)
    GenderRatio = models.IntegerField()
