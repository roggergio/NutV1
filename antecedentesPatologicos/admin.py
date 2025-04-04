from django.contrib import admin
from .models import AntecedentePatologico, OtraEnfermedad

class OtraEnfermedadInline(admin.TabularInline):
    model = OtraEnfermedad
    extra = 1

@admin.register(AntecedentePatologico)
class AntecedentePatologicoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha_registro']
    inlines = [OtraEnfermedadInline]
