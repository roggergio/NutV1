from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/<int:paciente_id>/alergias/', views.lista_alergias, name='lista_alergias'),
    path('pacientes/<int:paciente_id>/alergias/nueva/', views.agregar_alergia, name='agregar_alergia'),
    path('pacientes/<int:paciente_id>/alergias/editar/<int:alergia_id>/', views.editar_alergia, name='editar_alergia'),
    path('pacientes/<int:paciente_id>/alergias/eliminar/<int:alergia_id>/', views.eliminar_alergia, name='eliminar_alergia'),
]
