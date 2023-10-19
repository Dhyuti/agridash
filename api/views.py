from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Plant
from .serializers import PlantSerializer

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/plants/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of plants'
        },
        {
            'Endpoint': '/plants/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single plant object'
        },
        {
            'Endpoint': '/plants/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Adds new plants to the database'
        },
        {
            'Endpoint': '/plants/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing plant with new data'
        },
        {
            'Endpoint': '/plants/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing plant from the database '
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getPlants(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPlant(request, pk):
    plants = Plant.objects.get(id=pk)
    serializer = PlantSerializer(plants, many=False)
    return Response(serializer.data)