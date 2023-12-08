import factory
from factory.faker import faker
from food_trucks.models import (Applicant,
                                Location)
FAKE = faker.Faker()

query = Location.objects.all()

class ApplicantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Applicant
   

    @factory.lazy_attribute
    def location(self):
        max_value = len(query)-1
        index = FAKE.pyint(min_value=0, max_value=max_value)
        return query[index]
        
    @factory.lazy_attribute
    def applicant(self):
        return FAKE.company()
        
    facilityType = 'Truck'

    @factory.lazy_attribute
    def cnn(self):
        return FAKE.pyint(min_value=0, max_value=1000)
    

    @factory.lazy_attribute
    def locationDescription(self):
        return FAKE.sentence(nb_words=5)
        
    