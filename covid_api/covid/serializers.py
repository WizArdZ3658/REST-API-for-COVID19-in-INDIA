from rest_framework import serializers
from .models import AgeGroupDetails, HospitalBeds, ICMRTestingLabs, IndividualDetails, TestingDetails, Covid19India, \
    IndiaCensus


class AgeGroupDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroupDetails
        fields = ('agegrp', 'totalcases', 'percentage')


class HospitalBedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalBeds
        fields = (
            'StateUT',
            'NumPrimaryHealthCenters',
            'NumCommunityHealthCenters',
            'NumSubDistrictHospitals',
            'NumDistrictHospitals',
            'TotalPublicHealthFacilities',
            'NumPublicBeds',
            'NumRuralHospitals',
            'NumRuralBeds'
        )


class ICMRTestingLabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICMRTestingLabs
        fields = ('lab', 'address', 'pincode', 'City', 'StateUT', 'type')


class IndividualDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualDetails
        fields = (
            'government_id',
            'diagnosed_date',
            'age',
            'gender',
            'City',
            'detected_district',
            'StateUT',
            'nationality',
            'current_status'
        )


class TestingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingDetails
        fields = ('Date', 'StateUT', 'TotalSamples', 'Negative', 'Positive')


class IndiaCensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndiaCensus
        fields = ('StateUT', 'Population', 'Ruralpopulation', 'Urbanpopulation', 'Area', 'Density', 'GenderRatio')


class Covid19IndiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19India
        fields = (
            'Date',
            'Time',
            'StateUT',
            'ConfirmedIndianNational',
            'ConfirmedForeignNational',
            'Cured',
            'Deaths',
            'Confirmed'
        )