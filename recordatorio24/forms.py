from django import forms
from .models import Recordatorio24

class Recordatorio24Form(forms.ModelForm):
    class Meta:
        model = Recordatorio24
        fields = ['horario', 'descripcion', 'observaciones']
