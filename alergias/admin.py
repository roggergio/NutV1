from django.contrib import admin
from .models import Alergia

@admin.register(Alergia)
class AlergiaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'nombre', 'gravedad', 'fecha_diagnostico')
    list_filter = ('gravedad',)
    search_fields = ('nombre', 'paciente__nombre')
