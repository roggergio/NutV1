from django.contrib import admin
from .models import Recordatorio24

@admin.register(Recordatorio24)
class Recordatorio24Admin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'horario', 'descripcion', 'observaciones')
    list_filter = ('fecha', 'paciente')
    search_fields = ('paciente__nombre', 'descripcion', 'observaciones')
