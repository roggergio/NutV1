from django.contrib import admin
from .models import Enfermedad

@admin.register(Enfermedad)
class EnfermedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion_enfer', 'tratamiento_nut', 'nutriologo')
