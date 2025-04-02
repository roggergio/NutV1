from django.contrib import admin
from .models import HabitoAlimenticio

@admin.register(HabitoAlimenticio)
class HabitoAlimenticioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'alimento', 'cantidad', 'frecuencia', 'fecha_registro')
    list_filter = ('frecuencia', 'alimento')
    search_fields = ('paciente__nombre', 'alimento')
