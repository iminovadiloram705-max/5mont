from django.shortcuts import render

from rest_framework import viewsets
from .models import Model
from .serializers import CarModelSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = CarModelSerializer
