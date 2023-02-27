from rest_framework import serializers
from .models import *
class SerConverter(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'