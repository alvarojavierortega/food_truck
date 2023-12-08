from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from food_trucks.models import Applicant
from food_trucks.serializers import (ApplicantReaderSerializer,
                                     ApplicantWriterSerializer)
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@method_decorator(
    name='partial_update', 
    decorator=swagger_auto_schema(
    operation_description="Partial update",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'locationId': openapi.Schema(
                title='locationId',
                type=openapi.TYPE_INTEGER, 
                description='integer',
                example = 1),
            'applicant': openapi.Schema(
                title='applicant',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "Leo's Hot Dogs"),
            'facilityType': openapi.Schema(
                title='facilityType',
                type=openapi.TYPE_STRING, 
                description=str(Applicant.FACILITY_TYPE_CHOICES),
                example = 'Truck'),
            'cnn': openapi.Schema(
                title='cnn',
                type=openapi.TYPE_INTEGER, 
                description='integer',
                example = 9121000),
            'locationDescription': openapi.Schema(
                title='locationDescription',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "MISSION ST: 19TH ST to 20TH ST (2300 - 2399)" ),
            'address': openapi.Schema(
                title='address',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "2301 MISSION ST" ),
            'block': openapi.Schema(
                title='block',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "3595" ),
            'lot': openapi.Schema(
                title='lot',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "031"),
            'permit': openapi.Schema(
                title='permit',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "23MFF-00008" ),
            'status': openapi.Schema(
                title='status',
                type=openapi.TYPE_STRING, 
                description=str(Applicant.STATUS_CHOICES),
                enum=Applicant.STATUS_CHOICES,
                example = "APPROVED" ),
            'foodItems': openapi.Schema(
                title='foodItems',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "Hot dogs and related toppings: non alcoholic beverages"),
            'x': openapi.Schema(
                title='x',
                type=openapi.TYPE_NUMBER, 
                description='float',
                example = 6007018.02),
            'y': openapi.Schema(
                title='y',
                type=openapi.TYPE_NUMBER, 
                description='float',
                example = 2104913.057 ),
            'daysHours': openapi.Schema(
                title='daysHours',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "Mo-Fr:12PM-1PM" ),
            'NOISent': openapi.Schema(
                title='NOISent',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "" ),
            'schedule': openapi.Schema(
                title='schedule',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00008&ExportPDF=1&Filename=23MFF-00008_schedule.pdf" ),
            'approved': openapi.Schema(
                title='approved',
                type=openapi.TYPE_STRING, 
                description='datetime',
                example = "11/15/2024 12:00:00 AM" ),
            'received': openapi.Schema(
                title='received',
                type=openapi.TYPE_NUMBER, 
                description='integer',
                example = 20230920 ),
            'priorPermit': openapi.Schema(
                title='priorPermit',
                type=openapi.TYPE_INTEGER, 
                description=str(Applicant.Options.choices),
                enum=Applicant.Options.choices,
                example = 1),
            'expirationDate': openapi.Schema(
                title='expirationDate',
                type=openapi.TYPE_STRING, 
                description='datetime',
                example = "11/15/2024 12:00:00 AM" ),
            'firePreventionDistricts': openapi.Schema(
                title='firePreventionDistricts',
                type=openapi.TYPE_NUMBER, 
                description='integer',
                example = 2 ),
            'policeDistricts': openapi.Schema(
                title='policeDistricts',
                type=openapi.TYPE_NUMBER, 
                description='integer',
                example = 3 ),
            'supervisorDistricts': openapi.Schema(
                title='supervisorDistricts',
                type=openapi.TYPE_NUMBER, 
                description='integer',
                example = 4 ),
            'zipCode': openapi.Schema(
                title='zipCode',
                type=openapi.TYPE_NUMBER, 
                description='integer',
                example = 50502 ),
            'neighborhoodsOld': openapi.Schema(
                title='zipCode',
                type=openapi.TYPE_NUMBER, 
                description='integer',
                example = 20 ),


        }),
    responses={status.HTTP_201_CREATED: ApplicantReaderSerializer},
))
class ApplicantViewSet(viewsets.ModelViewSet):

    queryset = Applicant.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ApplicantReaderSerializer
        return ApplicantWriterSerializer