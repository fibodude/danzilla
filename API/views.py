from django.shortcuts import render
from .serializers import LevelSerializer 
from .models import Level
from rest_framework import routers, serializers, viewsets

# Create your views here.

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer





