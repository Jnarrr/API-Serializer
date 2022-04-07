from rest_framework import serializers
from . models import vehicles

class vehiclesSerializer(serializers.Hyperlinkmodelserializer):
    class meta:
        model = vehicles
        fields = ('name', 'description')