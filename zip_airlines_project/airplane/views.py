from django.shortcuts import render
from rest_framework import viewsets
from .models import Airplane
from .serializers import AirplaneSeriallizer

# Create your views here.
class AirplaneView(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSeriallizer
