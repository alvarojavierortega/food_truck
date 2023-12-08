from rest_framework import serializers
from food_trucks.models import Applicant, Location
from datetime import datetime

FORMAT_DATETIME = "%d/%m/%Y %H:%M:%S %P"

class ApplicantReaderSerializer(serializers.ModelSerializer):
    approved = serializers.DateTimeField(
        format=FORMAT_DATETIME)
    expirationDate = serializers.DateTimeField(
        format=FORMAT_DATETIME)

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
    
class CustomDateTimeField(serializers.DateTimeField):

    def to_internal_value(self, str_value):
        value = datetime.strptime(str_value, 'YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]')
        return value    
    
    def to_representation(self, value):
        return value.strftime(FORMAT_DATETIME)



class ApplicantWriterSerializer(serializers.ModelSerializer):
    locationId = LocationField(
        source='*')
    facilityType = serializers.ChoiceField(
        choices=Applicant.FACILITY_TYPE_CHOICES,
        help_text=str(Applicant.FACILITY_TYPE_CHOICES))
    status = serializers.ChoiceField(
        choices=Applicant.STATUS_CHOICES,
        help_text=str(Applicant.STATUS_CHOICES))
    approved = CustomDateTimeField()
    expirationDate = CustomDateTimeField()


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
            "locationDescription": "MISSION ST: 19TH ST to 20TH ST (2300 - 2399)", 
            "address": "2301 MISSION ST",
            "block": "3595",
            "lot": "031",
            "permit": "23MFF-00008",
            "status": "APPROVED",
            "foodItems": "Hot dogs and related toppings: non alcoholic beverages",
            "x": 6007018.02,
            "y": 2104913.057,
            "daysHours": "Mo-Fr:12PM-1PM",
            "NOISent": "",  
            "schedule": "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00008&ExportPDF=1&Filename=23MFF-00008_schedule.pdf",
            "approved": "11/15/2024 12:00:00 AM",
            "received": 20230920,
            "priorPermit": 1,
            "expirationDate": "11/15/2024 12:00:00 AM",
            "firePreventionDistricts": 2,
            "policeDistricts": 3,
            "supervisorDistricts": 4,
            "zipCode": 50502,
            "neighborhoodsOld": 20
        }
        return examples




