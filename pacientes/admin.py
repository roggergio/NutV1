from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'telefono', 'email', 'nutriologo', 'fecha_registro')
    search_fields = ('nombre', 'apellido_paterno', 'email', 'telefono')
    list_filter = ('genero', 'fecha_registro')
