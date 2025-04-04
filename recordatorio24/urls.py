from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/<int:paciente_id>/r24/', views.registrar_r24, name='registrar_r24'),
    path('pacientes/<int:paciente_id>/r24/ver/', views.ver_r24, name='ver_r24'),  # 👈 Nueva vista
]
