from django.shortcuts import render, get_object_or_404, redirect
from .models import Alergia
from .forms import AlergiaForm
from pacientes.models import Paciente
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

@login_required
def lista_alergias(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if paciente.nutriologo != request.user:
        raise PermissionDenied("No tienes permiso para ver este paciente.")
    alergias = paciente.alergias.all()
    return render(request, 'alergias/lista_alergias.html', {'paciente': paciente, 'alergias': alergias})

@login_required
def agregar_alergia(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    # Evita acceso no autorizado
    if paciente.nutriologo != request.user:
        raise Http404("No tienes permiso para agregar alergias a este paciente.")
    if request.method == 'POST':
        form = AlergiaForm(request.POST)
        if form.is_valid():
            alergia = form.save(commit=False)
            alergia.paciente = paciente  # Se asigna aquí, no desde el form
            alergia.save()
            return redirect('lista_alergias', paciente_id=paciente.id)
    else:
        form = AlergiaForm()

    return render(request, 'alergias/form_alergia.html', {
        'form': form,
        'paciente': paciente
    })


@login_required
def editar_alergia(request, paciente_id, alergia_id):
    alergia = get_object_or_404(Alergia, id=alergia_id, paciente__id=paciente_id)
    if paciente.nutriologo != request.user:
        raise PermissionDenied("No tienes permiso para ver este paciente.")
    paciente = alergia.paciente
    if request.method == 'POST':
        form = AlergiaForm(request.POST, instance=alergia)
        if form.is_valid():
            form.save()
            return redirect('lista_alergias', paciente_id=paciente.id)
    else:
        form = AlergiaForm(instance=alergia)
    return render(request, 'alergias/form_alergia.html', {'form': form, 'paciente': paciente})

@login_required
def eliminar_alergia(request, paciente_id, alergia_id):
    alergia = get_object_or_404(Alergia, id=alergia_id, paciente__id=paciente_id)
    
    alergia.delete()
    return redirect('lista_alergias', paciente_id=paciente_id)
