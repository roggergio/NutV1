from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/<int:paciente_id>/toxicomanias/', views.registrar_toxicomanias, name='registrar_toxicomanias'),
]
