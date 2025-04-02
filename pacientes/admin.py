from django.contrib import admin
from .models import Paciente

# Registro del modelo Paciente
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'telefono', 'email', 'nutriologo', 'fecha_registro')
    search_fields = ('nombre', 'apellido_paterno', 'email', 'telefono')
    list_filter = ('genero', 'fecha_registro')
    
    filter_horizontal = ()
    fieldsets = (
        (None, {
            'fields': ('nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'telefono', 'email', 'genero')
        }),
        ('Información adicional', {
            'fields': ('motivo_consulta', 'escolaridad', 'ocupacion', 'vegetariano', 'embarazo', 'deportista', 'adulto_mayor', 'pediatrico')
        }),
    )
