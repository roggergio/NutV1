from django.contrib import admin
from .models import Toxicomania

@admin.register(Toxicomania)
class ToxicomaniaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'alcohol', 'tabaco', 'otro_check')
    list_filter = ('alcohol', 'tabaco', 'otro_check', 'fecha')
    search_fields = ('paciente__nombre',)
