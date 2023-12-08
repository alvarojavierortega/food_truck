import factory
from factory.faker import faker
from food_trucks.models import Location
FAKE = faker.Faker()


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location
        django_get_or_create = ('latitude','longitude')


    @factory.sequence
    def latitude(n):
        return str(FAKE.latitude())

    @factory.sequence
    def longitude(n):
        return str(FAKE.longitude())
        

        
    