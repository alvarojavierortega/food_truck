from rest_framework import serializers
from food_trucks.models import Location
from .applicant import ApplicantReaderSerializer


class LocationReaderSerializer(serializers.ModelSerializer):
    applicants = ApplicantReaderSerializer(many=True)

    class Meta:
        model = Location
        fields =  '__all__'
    

class LocationWriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields =  '__all__'


    @staticmethod
    def get_examples():
        examples = { 
            "latitude": "37.76008693198698",
            "longitude": "-122.41880648110114",    
        }
        return examples




