from rest_framework import serializers
from food_trucks.models import Applicant, Location


class ApplicantReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields =  '__all__'
    

class LocationField(serializers.Field):

    def validate_locationId(self, value):
        if not Location.objects.filter(locationId=value).exists():
            raise serializers.ValidationError(f'Invalid pk \"{value}\" - object does not exist.')

    def to_internal_value(self, locationId):
        self.validate_locationId(locationId)
        value = {
            "location": Location.objects.get(locationId=locationId)
        }
        return value



class ApplicantWriterSerializer(serializers.ModelSerializer):
    locationId = LocationField(
        source='*')
    facilityType = serializers.ChoiceField(
        choices=Applicant.FACILITY_TYPE_CHOICES,
        help_text=str(Applicant.FACILITY_TYPE_CHOICES))

    class Meta:
        model = Applicant
        exclude = ["location"]
    
    def to_representation(self, instance):
        return ApplicantReaderSerializer(instance).data

    @staticmethod
    def get_examples():
        examples = { 
            "locationId": 1,
            "applicant": "Leo's Hot Dogs",
            "facilityType": "Truck",
            "cnn": 9121000,
            "locationDescription": "MISSION ST: 19TH ST to 20TH ST (2300 - 2399)"      
        }
        return examples




