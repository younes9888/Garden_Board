from rest_framework import serializers
from plants.models import Plant


class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plant
        fields='__all__'
