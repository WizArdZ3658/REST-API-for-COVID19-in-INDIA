from datetime import datetime
from .models import \
    AgeGroupDetails, \
    HospitalBeds, \
    IndividualDetails, \
    IndiaCensus, \
    ICMRTestingLabs, \
    TestingDetails, \
    Covid19India
import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .serializers import \
    AgeGroupDetailsSerializer, \
    HospitalBedsSerializer, \
    IndividualDetailsSerializer, \
    IndiaCensusSerializer, \
    ICMRTestingLabsSerializer, \
    TestingDetailsSerializer, \
    Covid19IndiaSerializer
import pandas as pd


def splitter(s):
    if '-' not in s and '.' not in s:
        return s
    elif '.' in s:
        return list(map(int, s.split('.')))[0]
    else:
        return sum(map(int, s.split('-'))) / 2


def foreign_national(t, mean):
    if '-' in t:
        return mean
    else:
        return int(t)


def date_formatter(d):
    d, m, y = d.split('/')
    return "20" + y + "-" + m + "-" + d


def ReloadAgeGroupDetails(request):
    AgeGroupDetails.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets\AgeGroupDetails.csv"), sep=',')
    for i in range(len(df)):
        _, created = AgeGroupDetails.objects.update_or_create(
            agegrp=df.iloc[i][1],
            totalcases=df.iloc[i][2],
            percentage=df.iloc[i][3],
        )
    return HttpResponse(status=204)


def ReloadHospitalBeds(request):
    HospitalBeds.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets\HospitalBedsIndia.csv"), sep=',')
    column_means = df.mean()
    df = df.fillna(column_means)

    for i in range(len(df)):
        _, created = HospitalBeds.objects.update_or_create(
            StateUT=df.iloc[i][1],
            NumPrimaryHealthCenters=df.iloc[i][2],
            NumCommunityHealthCenters=df.iloc[i][3],
            NumSubDistrictHospitals=df.iloc[i][4],
            NumDistrictHospitals=df.iloc[i][5],
            TotalPublicHealthFacilities=df.iloc[i][6],
            NumPublicBeds=df.iloc[i][7],
            NumRuralHospitals=df.iloc[i][8],
            NumRuralBeds=df.iloc[i][9],
            NumUrbanHospitals=df.iloc[i][10],
            NumUrbanBeds=df.iloc[i][11]
        )
    return HttpResponse(status=204)


def ReloadIndividualDetails(request):
    IndividualDetails.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets\IndividualDetails.csv"), sep=',')
    mode = df['age'].mode()[0]
    df['government_id'].fillna("", inplace=True)
    df['age'].fillna(mode, inplace=True)
    df['gender'].fillna("", inplace=True)
    df['detected_city'].fillna("", inplace=True)
    df['detected_district'].fillna("", inplace=True)
    df['detected_state'].fillna("", inplace=True)
    df['nationality'].fillna("", inplace=True)
    df['current_status'].fillna("", inplace=True)
    df['notes'].fillna("", inplace=True)
    df['diagnosed_date'] = df['diagnosed_date'].map(
        lambda diagnosed_date: datetime.strptime(diagnosed_date, '%d/%m/%Y').strftime('%Y-%m-%d'))
    df['age'] = df['age'].map(lambda age: splitter(str(age)))

    for i in range(len(df)):
        # print(df.iloc[i][0], df.iloc[i][3], sep=':', end=" ")
        _, created = IndividualDetails.objects.update_or_create(
            government_id=df.iloc[i][1],
            diagnosed_date=df.iloc[i][2],
            age=df.iloc[i][3],
            gender=df.iloc[i][4],
            City=df.iloc[i][5],
            detected_district=df.iloc[i][6],
            StateUT=df.iloc[i][7],
            nationality=df.iloc[i][8],
            current_status=df.iloc[i][9],
            notes=df.iloc[i][11]
        )
    return HttpResponse(status=204)


def ReloadIndiaCensus(request):
    IndiaCensus.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets\population_india_census2011.csv"), sep=',')
    for i in range(len(df)):
        _, created = IndiaCensus.objects.update_or_create(
            StateUT=df.iloc[i][1],
            Population=df.iloc[i][2],
            Ruralpopulation=df.iloc[i][3],
            Urbanpopulation=df.iloc[i][4],
            Area=df.iloc[i][5],
            Density=df.iloc[i][6],
            GenderRatio=df.iloc[i][7]
        )
    return HttpResponse(status=204)


def ReloadICMRTestingLabs(request):
    ICMRTestingLabs.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets\ICMRTestingLabs.csv"), sep=',')
    for i in range(len(df)):
        _, created = ICMRTestingLabs.objects.update_or_create(
            lab=df.iloc[i][0],
            address=df.iloc[i][1],
            pincode=df.iloc[i][2],
            City=df.iloc[i][3],
            StateUT=df.iloc[i][4],
            type=df.iloc[i][5]
        )
    return HttpResponse(status=204)


def ReloadTestingDetails(request):
    TestingDetails.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets\StatewiseTestingDetails.csv"), sep=',')
    for i in range(len(df)):
        neg = df.loc[i, 'Negative']
        pos = df.loc[i, 'Positive']
        tot = df.loc[i, 'TotalSamples']
        if neg != neg and pos != pos:
            neg = 0
            pos = 0
        elif neg != neg:
            neg = int(tot) - int(pos)
        elif pos != pos:
            pos = int(tot) - int(neg)

        if neg == ' ' and pos == ' ':
            neg = 0
            pos = 0
        elif neg == ' ':
            neg = int(tot) - int(pos)
        elif pos == ' ':
            pos = int(tot) - int(neg)

        _, created = TestingDetails.objects.update_or_create(
            Date=df.iloc[i][0],
            StateUT=df.iloc[i][1],
            TotalSamples=df.iloc[i][2],
            Negative=neg,
            Positive=pos
        )
    return HttpResponse(status=204)


def ReloadCovid19India(request):
    Covid19India.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets\covid_19_india.csv"), sep=',')
    df['Time'] = df['Time'].map(
        lambda Time: datetime.strptime(Time, "%I:%M %p").strftime("%H:%M"))
    df['Date'] = df['Date'].map(
        lambda Date: date_formatter(Date))

    for i in range(len(df)):
        # print(df.iloc[i])

        _, created = Covid19India.objects.update_or_create(
            Date=df.iloc[i][1],
            Time=df.iloc[i][2],
            StateUT=df.iloc[i][3],
            Cured=df.iloc[i][6],
            Deaths=df.iloc[i][7],
            Confirmed=df.iloc[i][8]
        )

    return HttpResponse(status=204)


class AgeGroupDetailsListAPIView(ListAPIView):
    serializer_class = AgeGroupDetailsSerializer
    queryset = AgeGroupDetails.objects.all()


class HospitalBedsListAPIView(ListAPIView):
    serializer_class = HospitalBedsSerializer
    queryset = HospitalBeds.objects.all()


class IndividualDetailsListAPIView(ListAPIView):
    serializer_class = IndividualDetailsSerializer
    queryset = IndividualDetails.objects.all()


class IndiaCensusListAPIView(ListAPIView):
    serializer_class = IndiaCensusSerializer
    queryset = IndiaCensus.objects.all()


class ICMRTestingLabsListAPIView(ListAPIView):
    serializer_class = ICMRTestingLabsSerializer
    queryset = ICMRTestingLabs.objects.all()


class TestingDetailsListAPIView(ListAPIView):
    serializer_class = TestingDetailsSerializer
    queryset = TestingDetails.objects.all()


class Covid19IndiaListAPIView(ListAPIView):
    serializer_class = Covid19IndiaSerializer
    queryset = Covid19India.objects.all()
