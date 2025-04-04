from django.urls import path
from . import views

urlpatterns = [
    path('paciente/<int:paciente_id>/antecedentes/', views.registrar_antecedentes, name='registrar_antecedentes'),
]