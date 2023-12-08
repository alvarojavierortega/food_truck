from django.db import models
from .location import Location

class Applicant(models.Model):
    FACILITY_TYPE_CHOICES = [
        ('Push Cart', 'Push Cart'),
        ('Truck', 'Truck')
    ]

    STATUS_CHOICES = [
        ('APPROVED', 'APPROVED'),
        ('REQUESTED', 'REQUESTED'),
        ('SUSPEND', 'SUSPEND'),
        ('EXPIRED', 'EXPIRED'),
        ('ISSUED', 'ISSUED')
    ]

    class Options(models.IntegerChoices):
        option0 = 0
        option1 = 1

    
    location = models.ForeignKey(
        Location, 
        db_column='location_id', 
        related_name='applicants', 
        on_delete=models.CASCADE)
    applicant = models.CharField(
        max_length=150,
        blank=True)  
    facilityType = models.CharField(
        max_length=9,
        choices=FACILITY_TYPE_CHOICES,
        blank=True
    )
    cnn = models.IntegerField(
        blank=True)
    locationDescription = models.CharField(
        max_length=150,
        blank=True)  
    address = models.CharField(
        max_length=150,
        blank=True)  
    block = models.CharField(
        max_length=150,
        blank=True)  
    lot = models.CharField(
        max_length=150,
        blank=True) 
    permit = models.CharField(
        max_length=150,
        blank=True)  
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        blank=True)
    foodItems = models.CharField(
        max_length=150,
        blank=True) 
    x = models.FloatField(
        blank=True)
    y = models.FloatField(
        blank=True)
    daysHours = models.CharField(
        max_length=150,
        blank=True) 
    NOISent = models.CharField(
        max_length=150,
        blank=True)
    schedule = models.CharField(
        max_length=150,
        blank=True) 
    approved = models.DateTimeField(
        blank=True)
    received = models.IntegerField(
        blank=True)
    priorPermit = models.IntegerField(
        choices=Options.choices,
        blank=True)
    expirationDate = models.DateTimeField(
        blank=True)
    firePreventionDistricts =  models.IntegerField(
        blank=True) 
    policeDistricts =  models.IntegerField(
        blank=True) 
    supervisorDistricts =  models.IntegerField(
        blank=True) 
    zipCode =  models.IntegerField(
        blank=True) 
    neighborhoodsOld=  models.SmallIntegerField(
        blank=True) 
    
    class Meta:
        db_table = "applicants"


