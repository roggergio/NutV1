from django.shortcuts import render, get_object_or_404, redirect
from .forms import ToxicomaniaForm
from pacientes.models import Paciente
from django.core.exceptions import PermissionDenied
from datetime import date
from .models import Toxicomania

def registrar_toxicomanias(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if paciente.nutriologo != request.user:
        raise PermissionDenied("No tienes permiso para ver este paciente.")

    hoy = date.today()
    instancia_existente = Toxicomania.objects.filter(paciente=paciente, fecha=hoy).first()

    if request.method == 'POST':
        form = ToxicomaniaForm(request.POST, instance=instancia_existente)
        if form.is_valid():
            toxicomania = form.save(commit=False)
            toxicomania.paciente = paciente
            toxicomania.fecha = hoy  # Asegura que conserve la fecha
            toxicomania.save()
            return redirect('detalle_paciente', paciente_id=paciente.id)
        else:
            print(form.errors)
    else:
        form = ToxicomaniaForm(instance=instancia_existente)

    return render(request, 'toxicomanias/registrar_toxicomanias.html', {
        'form': form,
        'paciente': paciente
    })
