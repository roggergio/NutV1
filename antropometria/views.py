from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Antropometria
from pacientes.models import Paciente
from .forms import AntropometriaForm

from decimal import Decimal, InvalidOperation
from django.utils.timezone import now
from django.core.exceptions import PermissionDenied
def to_decimal(value):
    try:
        return Decimal(value)
    except (TypeError, InvalidOperation):
        return None

@login_required
def registrar_antropometria(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if paciente.nutriologo != request.user:
        raise PermissionDenied("No tienes permiso para ver este paciente.")
    hoy = now().date()

    # Verifica si ya existe un registro para hoy
    antropometria = Antropometria.objects.filter(paciente=paciente, fecha=hoy).first()
    if paciente.nutriologo != request.user:
        raise PermissionDenied("No tienes permiso para ver este paciente.")

    if request.method == 'POST':
        peso = to_decimal(request.POST.get('peso'))
        estatura = to_decimal(request.POST.get('estatura'))
        cintura = to_decimal(request.POST.get('cintura'))
        cadera = to_decimal(request.POST.get('cadera'))
        grasa_corporal = to_decimal(request.POST.get('grasa_corporal'))
        masa_muscular = to_decimal(request.POST.get('masa_muscular'))

        if peso is None or estatura is None:
            return render(request, 'antropometria.html', {
                'paciente': paciente,
                'error': 'El Peso y la estatura son obligatorios.'
            })

        imc = peso / ((estatura / 100) ** 2)
        relacion_cc = (cintura / cadera) if cintura and cadera else None

        if antropometria:
            # Si ya existe, actualiza
            antropometria.peso = peso
            antropometria.estatura = estatura
            antropometria.imc = imc
            antropometria.cintura = cintura
            antropometria.cadera = cadera
            antropometria.relacion_cc = relacion_cc
            antropometria.grasa_corporal = grasa_corporal
            antropometria.masa_muscular = masa_muscular
            antropometria.save()
        else:
            # Si no existe, crea uno nuevo
            Antropometria.objects.create(
                paciente=paciente,
                peso=peso,
                estatura=estatura,
                imc=imc,
                cintura=cintura,
                cadera=cadera,
                relacion_cc=relacion_cc,
                grasa_corporal=grasa_corporal,
                masa_muscular=masa_muscular
            )

        return redirect('pacientes/datosPaciente.html', paciente_id=paciente.id)

    # En GET, enviar el registro de hoy si existe para prellenar el formulario
    return render(request, 'antropometria.html', {
        'paciente': paciente,
        'antropometria': antropometria
    })
