from django.contrib import admin
from .models import Bioquimico

@admin.register(Bioquimico)
class BioquimicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'valor_inferior_normal', 'valor_superior_normal')
    readonly_fields = [field.name for field in Bioquimico._meta.fields]
