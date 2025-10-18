from rest_framework import serializers
from .models import Model

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'
