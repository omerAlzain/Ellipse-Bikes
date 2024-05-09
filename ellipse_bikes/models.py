from django.contrib.gis.db import models
from django.utils import timezone


#A model representing a city.

class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# A model representing a contract.
    
class Contract(models.Model):
    name = models.CharField(max_length=200)
    commercial_name = models.CharField(max_length=200, blank=True, null=True)
    cities = models.ManyToManyField(City, blank=True)
    country_code = models.CharField(max_length=4, blank=True, null=True)

    def display_cities(self):
        if self.cities.count() > 2:
            return ', '.join([c.name for c in self.cities.all()[:3]]) + ' ...'
        elif self.cities.count() > 0:
            return ', '.join([c.name for c in self.cities.all()])
        else:
            return ''

    def __str__(self):
        return self.name

# A model representing a station.
    
class Station(models.Model):

    # Static data
    number = models.IntegerField("Station Number")
    # contract_name = models.CharField(max_length=200)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    position = models.PointField()
    shape = models.CharField(max_length=200, null=True, blank=True)
    overflow = models.BooleanField()
    banking = models.BooleanField()
    bonus = models.BooleanField()

    # Dynamic data
    # OPEN or CLOSED
    status = models.CharField(max_length=8)
    # "2024-05-01T19:17:07Z"
    last_update = models.DateTimeField()
    connected = models.BooleanField()

    # disponibilité des des vélos
    total_available_bikes = models.IntegerField()
    total_available_stands = models.IntegerField()
    total_available_mechanical_bikes = models.IntegerField()
    total_available_electrical_bikes = models.IntegerField()
    total_available_electrical_internal_battery_bikes = models.IntegerField()
    total_available_electrical_removable_battery_bikes = models.IntegerField()
    total_capacity = models.IntegerField()

    main_available_bikes = models.IntegerField()
    main_available_stands = models.IntegerField()
    main_available_mechanical_bikes = models.IntegerField()
    main_available_electrical_bikes = models.IntegerField()
    main_available_electrical_internal_battery_bikes = models.IntegerField()
    main_available_electrical_removable_battery_bikes = models.IntegerField()
    main_capacity = models.IntegerField()

    overflow_available_bikes = models.IntegerField(null=True, blank=True)
    overflow_available_stands = models.IntegerField(null=True, blank=True)
    overflow_available_mechanical_bikes = models.IntegerField(null=True, blank=True)
    overflow_available_electrical_bikes = models.IntegerField(null=True, blank=True)
    overflow_available_electrical_internal_battery_bikes = models.IntegerField(null=True, blank=True)
    overflow_available_electrical_removable_battery_bikes = models.IntegerField(null=True, blank=True)
    overflow_capacity = models.IntegerField(null=True, blank=True)

    last_schedule_run = models.DateTimeField()

    def contract_name(self):
        return self.contract.name

    def __str__(self):
        return self.name

