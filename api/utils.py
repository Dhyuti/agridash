from rest_framework.response import Response
from .models import Plant
from .serializers import PlantSerializer

def getPlantList(request):
    plants = Plant.objects.all().order_by('-updated')
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

def getPlantDetail(request, pk):
    try:
        plant = Plant.objects.get(id=pk)
    except Plant.DoesNotExist:
        return Response({'error': 'Plant not found'}, status=404)
    
    serializer = PlantSerializer(plant, many=False)
    return Response(serializer.data)

def createPlant(request):
    serializer = PlantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def updatePlant(request, pk):
    try:
        plant = Plant.objects.get(id=pk)
    except Plant.DoesNotExist:
        return Response({'error': 'Plant not found'}, status=404)
    
    serializer = PlantSerializer(instance=plant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

def deletePlant(request, pk):
    try:
        plant = Plant.objects.get(id=pk)
    except Plant.DoesNotExist:
        return Response({'error': 'Plant not found'}, status=404)
    
    plant.delete()
    return Response({'message': 'Plant was deleted!'}, status=204)
