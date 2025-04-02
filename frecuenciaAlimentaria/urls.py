from django.urls import path
from . import views

app_name = 'frecuenciaAlimentaria'

urlpatterns = [
     path('pacientes/<int:paciente_id>/registrarHabitos/', views.registrar_habitos, name='registrar_habitos'),
     path('pacientes/<int:paciente_id>/verHabitos/', views.ver_habitos, name='ver_habitos'),
]
