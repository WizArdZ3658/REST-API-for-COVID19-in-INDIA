from .views import \
    Reload, \
    AgeGroupDetailsListAPIView, \
    ICMRTestingLabsListAPIView, \
    IndiaCensusListAPIView, \
    Covid19IndiaListAPIView, \
    HospitalBedsListAPIView, \
    IndividualDetailsListAPIView, \
    TestingDetailsListAPIView
from django.urls import path

urlpatterns = [
    path('reload/', Reload, name="reload"),
    path('agegrp/', AgeGroupDetailsListAPIView.as_view(), name="age_grp_details_list"),
    path('testinglabs/', ICMRTestingLabsListAPIView.as_view(), name="testing_lab_details_list"),
    path('census/', IndiaCensusListAPIView.as_view(), name="india_census"),
    path('covid19india/', Covid19IndiaListAPIView.as_view(), name="covid19_india_list"),
    path('hospitals/', HospitalBedsListAPIView.as_view(), name="hospital_beds_details"),
    path('individualdetails/', IndividualDetailsListAPIView.as_view(), name="individual_details_list"),
    path('statetesting/', TestingDetailsListAPIView.as_view(), name="state_testing_details_list"),
]