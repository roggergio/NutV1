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

        def validar_campo(nombre_check, nombre_veces, nombre_frec, label):
            if cleaned_data.get(nombre_check):
                veces = cleaned_data.get(nombre_veces)
                frecuencia = cleaned_data.get(nombre_frec)

                if veces is None or veces < 1:
                    self.add_error(nombre_veces, f"El número de veces de {label} debe ser al menos 1.")
                if not frecuencia or frecuencia == 'nunca':
                    self.add_error(nombre_frec, f"Selecciona una frecuencia válida para {label}.")

        # ✅ Estas llamadas deben ir **dentro** de `clean`
        validar_campo('alcohol', 'alcohol_veces', 'alcohol_frecuencia', 'alcohol')
        validar_campo('tabaco', 'tabaco_veces', 'tabaco_frecuencia', 'tabaco')
        validar_campo('otro_check', 'otro_veces', 'otro_frecuencia', 'otro')

        if not (alcohol or tabaco or otro_check):
            raise forms.ValidationError("Debes seleccionar al menos una opción (alcohol, tabaco u otro).")

