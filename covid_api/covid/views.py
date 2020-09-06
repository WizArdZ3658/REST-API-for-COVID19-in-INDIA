import csv
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


def Reload(request):
    AgeGroupDetails.objects.all().delete()
    with open(os.path.join(settings.BASE_DIR, "datasets\AgeGroupDetails.csv")) as f:
        reader = csv.reader(f)
        flag = True
        for row in reader:
            if flag:
                flag = False
                continue
            # print(row)
            _, created = AgeGroupDetails.objects.update_or_create(
                agegrp=row[1],
                totalcases=row[2],
                percentage=row[3],
            )

    return HttpResponse(status=204)


class AgeGroupDetailsListAPIView(ListAPIView):
    serializer_class = AgeGroupDetailsSerializer
    queryset = AgeGroupDetails.objects.all()


class HospitalBedsListAPIView(ListAPIView):
    serializer_class = HospitalBedsSerializer
    queryset = HospitalBeds


class IndividualDetailsListAPIView(ListAPIView):
    serializer_class = IndividualDetailsSerializer
    queryset = IndividualDetails


class IndiaCensusListAPIView(ListAPIView):
    serializer_class = IndiaCensusSerializer
    queryset = IndiaCensus


class ICMRTestingLabsListAPIView(ListAPIView):
    serializer_class = ICMRTestingLabsSerializer
    queryset = ICMRTestingLabs


class TestingDetailsListAPIView(ListAPIView):
    serializer_class = TestingDetailsSerializer
    queryset = TestingDetails


class Covid19IndiaListAPIView(ListAPIView):
    serializer_class = Covid19IndiaSerializer
    queryset = Covid19India
