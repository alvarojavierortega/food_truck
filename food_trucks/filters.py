from food_trucks.models import Location
import django_filters

class LocationFilter(django_filters.FilterSet):
    
    class Meta:
        model = Location
        fields = ['latitude', 'longitude']