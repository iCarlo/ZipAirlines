from django.db import models


class Airplanes(models.Model):
    model_id = models.IntegerField()
    name = models.CharField(max_length=100)
    number_of_passengers = models.IntegerField()
    fuel_capacity = models.IntegerField()
    total_fuel_consumption_per_minute = models.FloatField()
    maximum_flight_time = models.FloatField()

    def __str__(self):
        return self.name