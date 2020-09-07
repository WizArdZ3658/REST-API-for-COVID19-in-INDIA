from .views import \
    AgeGroupDetailsListAPIView, \
    ICMRTestingLabsListAPIView, \
    IndiaCensusListAPIView, \
    Covid19IndiaListAPIView, \
    HospitalBedsListAPIView, \
    IndividualDetailsListAPIView, \
    TestingDetailsListAPIView, \
    ReloadAgeGroupDetails, \
    ReloadCovid19India, \
    ReloadHospitalBeds, \
    ReloadICMRTestingLabs, \
    ReloadIndiaCensus, \
    ReloadIndividualDetails, \
    ReloadTestingDetails
from django.urls import path

urlpatterns = [
    path('reload/agegrp/', ReloadAgeGroupDetails, name="reload_agegrp"),
    path('reload/testinglabs/', ReloadICMRTestingLabs, name="reload_testing_labs"),
    path('reload/census/', ReloadIndiaCensus, name="reload_census"),
    path('reload/covid19india/', ReloadCovid19India, name="reload_covid19_india"),
    path('reload/hospitals/', ReloadHospitalBeds, name="reload_hospitals"),
    path('reload/individualdetails/', ReloadIndividualDetails, name="reload_indi_details"),
    path('reload/statetesting/', ReloadTestingDetails, name="reload_testing_details"),
    path('agegrp/', AgeGroupDetailsListAPIView.as_view(), name="age_grp_details_list"),
    path('testinglabs/', ICMRTestingLabsListAPIView.as_view(), name="testing_lab_details_list"),
    path('census/', IndiaCensusListAPIView.as_view(), name="india_census"),
    path('covid19india/', Covid19IndiaListAPIView.as_view(), name="covid19_india_list"),
    path('hospitals/', HospitalBedsListAPIView.as_view(), name="hospital_beds_details"),
    path('individualdetails/', IndividualDetailsListAPIView.as_view(), name="individual_details_list"),
    path('statetesting/', TestingDetailsListAPIView.as_view(), name="state_testing_details_list"),
]