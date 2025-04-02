from django import forms
from .models import HabitoAlimenticio, FRECUENCIA_CHOICES

class HabitoAlimenticioForm(forms.ModelForm):
    class Meta:
        model = HabitoAlimenticio
        fields = ['alimento', 'cantidad', 'frecuencia']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 10}),
            'frecuencia': forms.Select(choices=FRECUENCIA_CHOICES),
        }
