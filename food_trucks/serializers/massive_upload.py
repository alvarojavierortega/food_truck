from rest_framework import serializers
from food_trucks.models import Applicant, Location
from .applicant import ApplicantReaderSerializer, CustomDateTimeField


class MassiveUploadDataSerializer(serializers.ModelSerializer):
    locationId = serializers.IntegerField()
    latitude = serializers.DecimalField(max_digits=20, decimal_places=17)
    longitude = serializers.DecimalField(max_digits=20, decimal_places=17)
    facilityType = serializers.ChoiceField(
        choices=Applicant.FACILITY_TYPE_CHOICES,
        help_text=str(Applicant.FACILITY_TYPE_CHOICES))
    approved = CustomDateTimeField()
    expirationDate = CustomDateTimeField()

    class Meta:
        model = Applicant
        exclude = ["location"]

    def validate(self, data):
        data = super().validate(data)
        location_data = {
            "locationId": data.pop('locationId'),
            "latitude":  data.pop('latitude'),
            "longitude": data.pop('longitude')
        }
        try:
            location, _ = Location.objects.get_or_create(**location_data)
        except:
            location_data.pop("locationId")
            location, _ = Location.objects.get_or_create(**location_data)
        data['location'] = location
        return data
    
    def to_representation(self, instance):
        return ApplicantReaderSerializer(instance).data






