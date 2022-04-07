from rest_framework import serializers
from . models import vehicles

class vehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vehicles
        fields = ('id', 'name', 'description')