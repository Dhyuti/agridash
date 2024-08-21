from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('plant/index', views.index, name='index'),
    path('plant/<int:id>/', views.plant_detail, name='plant_detail'),
    path('plant/create/', views.create_plant, name='create_plant'),
    path('plant/<int:id>/delete/', views.delete_plant, name='delete_plant'),
    path('plant/<int:id>/update/', views.update_plant, name='update_plant'),
]
