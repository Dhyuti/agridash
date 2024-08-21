from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.getRoutes, name="routes"),
    path('api/plants/', views.getPlants, name="plants"),
    path('api/plants/<str:pk>/', views.getPlant, name="plant"),
]
