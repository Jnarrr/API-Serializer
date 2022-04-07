from django.shortcuts import render
from rest_framework import viewsets
from . serializers import vehiclesSerializer
from . models import vehicles

class vehiclesViewSet(viewsets.ModelViewSet):
    queryset = vehicles.objects.all().order_by('name')
    serializer_class = vehiclesSerializer

# Create your views here.
