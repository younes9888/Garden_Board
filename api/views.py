from rest_framework.views import APIView
from rest_framework.response import Response

from plants.models import Plant
from .serializers import PlantsSerializer

# Create your views here.

class PlantsListApiView(APIView):
    def get(self,request,format=None):
        plants=Plant.objects.all()
        serialized_plants=PlantsSerializer(plants,many=True)
        return Response(serialized_plants.data)


class PlantsDetailApiView(APIView):
    def get(self,request,id,format=None):
        plant=Plant.objects.get(id=id)
        serialized_plant=PlantsSerializer(plant)
        return Response(serialized_plant.data)