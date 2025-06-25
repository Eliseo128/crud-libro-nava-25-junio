from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('editar_libro/<int:id>/', views.editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    path('actualizar_libro/<int:id>/', views.actualizar_libro, name='actualizar_libro'),
]

