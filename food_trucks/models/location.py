from django.db import models



class Location(models.Model):
    locationId = models.AutoField(
        primary_key=True)
    latitude = models.DecimalField(
        max_digits=20, 
        decimal_places=17) 
    longitude = models.DecimalField(
        max_digits=20, 
        decimal_places=17) 
    
    def __str__(self):
        return f"lat: {self.latitude}, lon: {self.longitude}"
    
    class Meta:
        db_table = "locations"

        constraints = [
            models.UniqueConstraint(
                fields=['latitude',
                        'longitude'], 
                name='unique_coordinates'),
        ]

