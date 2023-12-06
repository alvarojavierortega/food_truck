from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters import rest_framework as filters
from food_trucks.models import Location
from food_trucks.serializers import (LocationReaderSerializer,
                                     LocationWriterSerializer)
from food_trucks.filters import LocationFilter
from rest_framework import viewsets, status

@method_decorator(
    name='partial_update', 
    decorator=swagger_auto_schema(
    operation_description="Partial update",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'latitude': openapi.Schema(
                title='latitude',
                type=openapi.TYPE_NUMBER, 
                description='Number',
                example = "-2.157876"),
            'longitude': openapi.Schema(
                title='longitude',
                type=openapi.TYPE_NUMBER, 
                description='Number',
                example = "30.229906"),
        }),
    responses={status.HTTP_201_CREATED: LocationReaderSerializer},
))
class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LocationFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LocationReaderSerializer
        return LocationWriterSerializer