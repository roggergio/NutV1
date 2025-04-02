from django.shortcuts import render, redirect, get_object_or_404
from .models import HabitoAlimenticio
from .forms import HabitoAlimenticioForm
from pacientes.models import Paciente

ALIMENTOS = [
    "Verduras", "Frutas", "Pan Dulce", "Tortilla", "Avena",
    "Leguminosas", "Pollo", "Pescado", "Res", "Puerco",
    "Queso", "Leche", "Aceites y Grasas", "Azúcar",
    "Refresco", "Agua de Sabor", "Galletas", "Alcohol"
]

def registrar_habitos(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)

    if request.method == 'POST':
        for alimento in ALIMENTOS:
            cantidad = request.POST.get(f'{alimento}_cantidad')
            frecuencia = request.POST.get(f'{alimento}_frecuencia')
            if cantidad is not None and frecuencia:
                HabitoAlimenticio.objects.create(
                    paciente=paciente,
                    alimento=alimento,
                    cantidad=int(cantidad),
                    frecuencia=frecuencia
                )
        return redirect('lista_pacientes')  # Ajusta al nombre real de tu vista

    context = {
        'alimentos': ALIMENTOS,
        'paciente': paciente
    }
    return render(request, 'frecuenciaAlimentaria/registrarHabitos.html', context)

def ver_habitos(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    habitos = HabitoAlimenticio.objects.filter(paciente=paciente).order_by('alimento')

    context = {
        'paciente': paciente,
        'habitos': habitos,
    }
    return render(request, 'frecuenciaAlimentaria/verHabitos.html', context)