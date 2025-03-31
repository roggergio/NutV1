from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Antropometria, Paciente
from .forms import PacienteForm, AntropometriaForm
from django.db.models import Q
from decimal import Decimal, InvalidOperation
from django.utils.timezone import now

@login_required
def lista_pacientes(request):
    query = request.GET.get('q')
    if query:
        pacientes = Paciente.objects.filter(
            Q(nutriologo=request.user) &
            (
                Q(nombre__icontains=query) |
                Q(apellido_paterno__icontains=query) |
                Q(apellido_materno__icontains=query) |
                Q(email__icontains=query)
            )
        )
    else:
        pacientes = Paciente.objects.filter(nutriologo=request.user)

    return render(request, 'pacientes/lista_pacientes.html', {
        'pacientes': pacientes,
        'query': query,
    })

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.nutriologo = request.user  # Asignar el nutriólogo actual
            paciente.save()
            messages.success(request, 'Paciente registrado correctamente.')
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, nutriologo=request.user)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.nutriologo = request.user
            paciente.save()
            messages.success(request, 'Paciente actualizado correctamente.')
            return redirect('lista_pacientes')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = PacienteForm(instance=paciente)
    
    return render(request, 'pacientes/crear_paciente.html', {'form': form, 'paciente': paciente})

@login_required
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, nutriologo=request.user)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado correctamente.')
        return redirect('lista_pacientes')
    return render(request, 'pacientes/confirmar_eliminar.html', {'paciente': paciente})

@login_required
def datos_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'pacientes/datosPaciente.html', {'paciente': paciente})



#---------------------------------------------------------------------------------------Antropometría
def to_decimal(value):
    try:
        return Decimal(value)
    except (TypeError, InvalidOperation):
        return None

def registrar_antropometria(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    hoy = now().date()

    # Verifica si ya existe un registro para hoy
    antropometria = Antropometria.objects.filter(paciente=paciente, fecha=hoy).first()

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
                'error': 'Peso y estatura son obligatorios y deben ser números.'
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
