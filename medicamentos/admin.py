# medicamentos/admin.py
from django.contrib import admin
from .models import Medicamento

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        'paciente',
        'nombre_farmaco',
        'nombre_generico',
        'presentacion',
        'dosis',
        'frecuencia',
        'duracion',
        'via',
        'observaciones',
    )
    search_fields = ['nombre_farmaco', 'nombre_generico', 'paciente__nombre']
    list_filter = ['frecuencia', 'via']

admin.site.register(Medicamento, MedicamentoAdmin)
