from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from .forms import PlantForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import getPlantList, getPlantDetail, createPlant, updatePlant, deletePlant

# HTML Views

def base(request):
    return render(request, 'base.html')

def index(request):
    plants = Plant.objects.all()
    return render(request, 'index.html', {'plants': plants})

def plant_detail(request, id):
    plant = get_object_or_404(Plant, id=id)
    return render(request, 'plant.html', {'plant': plant})

def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PlantForm()
    return render(request, 'create_plant.html', {'form': form})

def delete_plant(request, id):
    plant = get_object_or_404(Plant, id=id)
    if request.method == 'POST':
        plant.delete()
        return redirect('index')
    return render(request, 'delete_plant.html', {'plant': plant})

def update_plant(request, id):
    plant = get_object_or_404(Plant, id=id)
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', id=id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'update_plant.html', {'form': form, 'plant': plant})

# API Views

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
            'Endpoint': '/plants/<str:pk>/',
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
            'Endpoint': '/plants/<str:pk>/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing plant with new data'
        },
        {
            'Endpoint': '/plants/<str:pk>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing plant from the database '
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getPlants(request):
    return getPlantList(request)

@api_view(['GET'])
def getPlant(request, pk):
    return getPlantDetail(request, pk)

@api_view(['POST'])
def createPlant(request):
    return createPlant(request)

@api_view(['PUT'])
def updatePlant(request, pk):
    return updatePlant(request, pk)

@api_view(['DELETE'])
def deletePlant(request, pk):
    return deletePlant(request, pk)
