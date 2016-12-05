from django.conf.urls import url, include
from .models import Level
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'author', 'data')
