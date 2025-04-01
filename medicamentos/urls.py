# medicamentos/urls.py
from django.urls import path
from . import views

app_name = 'medicamentos'

urlpatterns = [
    path('pacientes/<int:paciente_id>/registrar/', views.registrar_medicamentos, name='registrar'),
    path('pacientes/<int:paciente_id>/medicamentos/', views.lista_medicamentos, name='lista'),

]
