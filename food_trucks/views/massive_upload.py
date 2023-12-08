

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from food_trucks.utils import read_csv_file
from food_trucks.serializers import MassiveUploadDataSerializer
null_request_body = serializers.Serializer

MAP_KEYS = {
    "locationid" : "locationId",
    "Applicant"  : "applicant",
    "FacilityType": "facilityType",
    "cnn": "cnn",
    "LocationDescription": "locationDescription",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Address": "address",
    "block": "block",
    "lot": "lot",
    "permit": "permit", 
    "Status": "status",
    "FoodItems": "foodItems", 
    "X": "x", 
    "Y": "y",
    "Schedule": "schedule", 
    "dayshours": "daysHours",
    "NOISent": "NOISent", 
    "Approved": "approved", 
    "Received": "received", 
    "PriorPermit": "priorPermit", 
    "ExpirationDate": "expirationDate", 
    "Fire Prevention Districts": "firePreventionDistricts", 
    "Police Districts": "policeDistricts", 
    "Supervisor Districts": "supervisorDistricts",
    "Zip Codes": "zipCode",
    "Neighborhoods (old)": "neighborhoodsOld"

}


class MassiveUploadData(APIView):

    serializer_class = MassiveUploadDataSerializer
    parser_classes = (MultiPartParser,FileUploadParser)

    def __filter_csv_data(self, file_info:list):
        return [data for data in file_info if data.get("FacilityType")=="Truck"]

    def __map_csv_data(self, csv_data:dict) -> dict:
        data = {MAP_KEYS[key]:value for key, value in csv_data.items() if key in MAP_KEYS}
        return data
       

    @swagger_auto_schema(
        operation_description='Upload data from CSV file',
        methods=['POST'], 
        manual_parameters=[
            openapi.Parameter(
                name="file",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description="CSV file"
                )
            ],
        request_body=null_request_body,
        responses={status.HTTP_400_BAD_REQUEST: 'A JSON  with the detailed errors is provided.',
                   status.HTTP_201_CREATED: 'Successfully upload the data'},                
    )
    @action(
        detail=False, 
        methods=['POST'], 
        parser_classes = (MultiPartParser,FileUploadParser))
    def post(self, request):
        file = request.FILES.get("file")
        file_info = read_csv_file(file)
        file_info = self.__filter_csv_data(file_info)
        errors = False
        content = {'errors' : []}
        for data in file_info:
            data = self.__map_csv_data(data)
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                data.update({"errors": serializer.errors})
                content['errors'].append(data)
                errors = True
            else:
                serializer.save()
        if errors:
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response("Successfully uploaded data", status=status.HTTP_201_CREATED)
    


