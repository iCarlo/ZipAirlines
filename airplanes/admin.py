from django.contrib import admin
from .models import Airplanes


@admin.register(Airplanes)
class AirplanesAdmin(admin.ModelAdmin):
    list_display = ['model_id', 'name', 'number_of_passengers', 'maximum_flight_time']
