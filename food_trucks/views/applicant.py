from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from food_trucks.models import Applicant
from food_trucks.serializers import (ApplicantReaderSerializer,
                                     ApplicantWriterSerializer)
from rest_framework import viewsets, status


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
                enum=Applicant.FACILITY_TYPE_CHOICES,
                example = 'Truck'),
            'cnn': openapi.Schema(
                title='cnn',
                type=openapi.TYPE_INTEGER, 
                description='integer',
                example = 9121000),
            'applicant': openapi.Schema(
                title='applicant',
                type=openapi.TYPE_STRING, 
                description='string',
                example = "MISSION ST: 19TH ST to 20TH ST (2300 - 2399)" ),
        }),
    responses={status.HTTP_201_CREATED: ApplicantReaderSerializer},
))
class ApplicantViewSet(viewsets.ModelViewSet):

    queryset = Applicant.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ApplicantReaderSerializer
        return ApplicantWriterSerializer