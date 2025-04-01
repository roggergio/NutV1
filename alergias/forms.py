from django import forms
from .models import Alergia

class AlergiaForm(forms.ModelForm):
    fecha_diagnostico = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Alergia
        exclude = ['paciente']
