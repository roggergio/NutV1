from django.urls import path
from . import views

urlpatterns = [
    path('paciente/<int:paciente_id>/antropometria/', views.registrar_antropometria, name='registrar_antropometria'),
]