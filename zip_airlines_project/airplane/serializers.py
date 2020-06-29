from rest_framework import serializers
from .models import Airplane
import math


class AirplaneSeriallizer(serializers.ModelSerializer):
    fuel_consumption = serializers.SerializerMethodField(method_name='get_consumption_per_minute')
    maximum_minutes = serializers.SerializerMethodField(method_name='get_maximum_minutes')
    class Meta:
        model = Airplane
        fields = ('url','airplane_id', 'passenger', 'fuel_consumption', 'maximum_minutes')

    
    def get_consumption_per_minute(self, instance):
        """Return the fuel consumption per minute"""
        # passenger has 0.20 consumption and multiply the total # of passenger to get the total passenger consumption
        passenger_consumption = instance.passenger * 0.002

        # apc = id * (0.80 + 0.002)
        # add up the total passenger consumption to aiplane consumption 0.80
        airplane_consumption = instance.airplane_id * (0.80 + passenger_consumption)

        return str(airplane_consumption) + ' liters per minute'
    
    def get_maximum_minutes(self, instance):
        """Return the Maximum travel time"""
        # multiply the aiplane id to fuel tank to get the fuel tank capacity
        fuel_tank_capacity = instance.airplane_id * 200

        # multiply the # of passsenger to 0.20 to get the total of passenger consumption
        passenger_consumption = instance.passenger * 0.002 

        # add airplane fuel consumption and passenger consumption then multiply to get the total airplane fuel consumption
        airplane_consumption = instance.airplane_id * (0.80 + passenger_consumption) 

        maximum_minutes = (fuel_tank_capacity/airplane_consumption) * 60

        return str(maximum_minutes) + ' minutes'