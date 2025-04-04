from django import forms
from .models import AntecedentePatologico, OtraEnfermedad, FAMILIARES, ENFERMEDADES_BASE

class AntecedentePatologicoForm(forms.ModelForm):
    class Meta:
        model = AntecedentePatologico
        fields = ['diabetes', 'hipertension', 'colesterolemia', 'trigliceridemia', 'obesidad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for enfermedad in ENFERMEDADES_BASE:
            self.fields[enfermedad[0]] = forms.MultipleChoiceField(
                choices=FAMILIARES,
                widget=forms.CheckboxSelectMultiple,
                label=enfermedad[1],
                required=False
            )


class OtraEnfermedadForm(forms.ModelForm):
    class Meta:
        model = OtraEnfermedad
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Nombre de la enfermedad'})
        for familiar, label in FAMILIARES:
            self.fields[familiar] = forms.BooleanField(label=label, required=False)
