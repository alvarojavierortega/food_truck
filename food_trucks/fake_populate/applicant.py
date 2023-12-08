import factory
from factory.faker import faker
from food_trucks.models import (Applicant,
                                Location)
import pytz
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
    
    @factory.lazy_attribute
    def address(self):
        return FAKE.address()
    
    @factory.lazy_attribute
    def block(self):
        return FAKE.building_number()
    

    @factory.lazy_attribute
    def lot(self):
        return FAKE.building_number()

    @factory.lazy_attribute
    def status(self):
        options = ["APPROVED", 
                   "REQUESTED", 
                   "SUSPEND", "EXPIRED", 
                   "ISSUED"]
        index = FAKE.pyint(min_value=0, max_value=3)
        return options[index]

    
    @factory.lazy_attribute
    def foodItems(self):
        return FAKE.sentence(nb_words=5)
    
    @factory.lazy_attribute
    def x(self):
        return FAKE.pyfloat()
    
    @factory.lazy_attribute
    def y(self):
        return FAKE.pyfloat()
    
    @factory.lazy_attribute
    def daysHours(self):
        return FAKE.day_of_week()
    
    NOISent = ""

    schedule = "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00008&ExportPDF=1&Filename=23MFF-00008_schedule.pdf",
      
    @factory.lazy_attribute
    def approved(self):
        return FAKE.date_time(tzinfo=pytz.UTC)

    @factory.lazy_attribute
    def received(self):
        return FAKE.pyint(min_value=0, max_value=100)

    priorPermit = 1

    @factory.lazy_attribute
    def expirationDate(self):
        return FAKE.date_time(tzinfo=pytz.UTC)

    @factory.lazy_attribute
    def firePreventionDistricts(self):
        return FAKE.pyint(min_value=0, max_value=100)


    @factory.lazy_attribute
    def policeDistricts(self):
        return FAKE.pyint(min_value=0, max_value=100)


    @factory.lazy_attribute
    def supervisorDistricts(self):
        return FAKE.pyint(min_value=0, max_value=100)


    @factory.lazy_attribute
    def zipCode(self):
        return FAKE.pyint(min_value=0, max_value=100)



    @factory.lazy_attribute
    def neighborhoodsOld(self):
        return FAKE.pyint(min_value=0, max_value=100)
    

    

        
    