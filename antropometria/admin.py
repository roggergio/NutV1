from django.contrib import admin
from .models import Antropometria
# Register your models here.
# Registro del modelo Antropometria
@admin.register(Antropometria)
class AntropometriaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'peso', 'estatura', 'imc', 'fecha')
    search_fields = ('paciente__nombre', 'paciente__apellido_paterno', 'paciente__email')
    list_filter = ('fecha',)
    readonly_fields = ('imc', 'relacion_cc')  # Para que estos campos no se editen en el admin