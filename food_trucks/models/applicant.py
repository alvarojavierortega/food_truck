from django.db import models
from .location import Location

class Applicant(models.Model):
    FACILITY_TYPE_CHOICES = [
        ('Push Cart', 'Push Cart'),
        ('Truck', 'Truck')
    ]
    location = models.ForeignKey(
        Location, 
        db_column='location_id', 
        related_name='applicants', 
        on_delete=models.CASCADE)
    applicant = models.CharField(
        max_length=150)  
    facilityType = models.CharField(
        max_length=9,
        choices=FACILITY_TYPE_CHOICES,
        blank=True
    )
    cnn = models.IntegerField()
    locationDescription = models.CharField(
        max_length=150,
        blank=True)  

    
    class Meta:
        db_table = "applicants"


"""
  locationid, int
  Applicant, str
  FacilityType, enum(Push Cart, Truck) blank
  cnn, int
  LocationDescription, str, blank
  Address, str
  blocklot, ?
  block,lot, str, str short blank
  permit, str
  Status, enum(APPROVED, REQUESTED, SUSPEND, EXPIRED, ISSUED)
  FoodItems, str
  X, float, 5 decimals, blank
  Y, float, 5 decimals, blank
  Latitude, 0?
  Longitude,
  Schedule, link
  dayshours, str, blank
  NOISent, str, all blanks
  Approved, datetime, blank
  Received, int
  PriorPermit, enum(0,1)
  ExpirationDate, datetime, blank
  Location, ?
  Fire Prevention Districts, int, blank 
  Police Districts, int blank 
  Supervisor Districts, int  blank 
  Zip Codes, int blank 
  Neighborhoods (old) int blank 

   
"""
