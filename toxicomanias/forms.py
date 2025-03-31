from django import forms
from .models import Toxicomania

class ToxicomaniaForm(forms.ModelForm):
    class Meta:
        model = Toxicomania
        exclude = ['paciente']

    def clean(self):
        cleaned_data = super().clean()
        alcohol = cleaned_data.get('alcohol')
        tabaco = cleaned_data.get('tabaco')
        otro_check = cleaned_data.get('otro_check')

        # Validaciones específicas solo si están activados los campos
        if alcohol:
            if not cleaned_data.get('alcohol_veces'):
                self.add_error('alcohol_veces', 'Este campo es obligatorio.')
            if not cleaned_data.get('alcohol_frecuencia') or cleaned_data.get('alcohol_frecuencia') == 'nunca':
                self.add_error('alcohol_frecuencia', 'Selecciona una frecuencia válida.')

        if tabaco:
            if not cleaned_data.get('tabaco_veces'):
                self.add_error('tabaco_veces', 'Este campo es obligatorio.')
            if not cleaned_data.get('tabaco_frecuencia') or cleaned_data.get('tabaco_frecuencia') == 'nunca':
                self.add_error('tabaco_frecuencia', 'Selecciona una frecuencia válida.')

        if otro_check:
            if not cleaned_data.get('otro'):
                self.add_error('otro', 'Indica el tipo de sustancia.')
            if not cleaned_data.get('otro_veces'):
                self.add_error('otro_veces', 'Este campo es obligatorio.')
            if not cleaned_data.get('otro_frecuencia') or cleaned_data.get('otro_frecuencia') == 'nunca':
                self.add_error('otro_frecuencia', 'Selecciona una frecuencia válida.')

        # Si no seleccionó ninguna sustancia
        if not (alcohol or tabaco or otro_check):
            raise forms.ValidationError("Debes seleccionar al menos una opción (alcohol, tabaco u otro).")
