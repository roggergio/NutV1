from django.urls import path
from . import views

urlpatterns = [
    path('lista_pacientes', views.lista_pacientes, name='lista_pacientes'),
    path('crear_paciente', views.crear_paciente, name='crear_paciente'),
    path('editar/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
]
