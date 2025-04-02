from django import forms
from .models import Enfermedad

class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = ['nombre', 'descripcion_enfer', 'tratamiento_nut', 'bibliografia', 'link']
