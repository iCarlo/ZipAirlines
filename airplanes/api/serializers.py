from rest_framework import serializers

from ..models import Airplanes


class AirplanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplanes
        fields = '__all__'

