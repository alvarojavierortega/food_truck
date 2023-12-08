from django.urls import path, include
from rest_framework.routers import DefaultRouter
from food_trucks import views

router = DefaultRouter()
router.register(r'applicants', views.ApplicantViewSet, basename="applicant")
router.register(r'locations', views.LocationViewSet, basename="location")

urlpatterns = [
    path('', include(router.urls)),
    path('upload-data/', 
         views.MassiveUploadData.as_view(), 
         name='upload_data'),
]