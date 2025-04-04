from django.shortcuts import render, get_object_or_404, redirect
from .models import AntecedentePatologico, OtraEnfermedad
from pacientes.models import Paciente

enfermedades_base = [
    {"name": "diabetes", "label": "Diabetes"},
    {"name": "hipertension", "label": "Hipertensión"},
    {"name": "colesterolemia", "label": "Colesterolemia"},
    {"name": "trigliceridemia", "label": "Trigliceridemia"},
    {"name": "obesidad", "label": "Obesidad"},
]

familiares = [
    ("paciente", "Paciente"),
    ("padre", "Padre"),
    ("madre", "Madre"),
    ("abuelos_paternos", "Abuelos paternos"),
    ("abuelos_maternos", "Abuelos maternos"),
    ("hermanos", "Hermanos"),
]

def registrar_antecedentes(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    antecedentes, created = AntecedentePatologico.objects.get_or_create(paciente=paciente)

    if request.method == 'POST':
        # Enfermedades base
        for enfermedad in [e["name"] for e in enfermedades_base]:
            enfermedad_dict = {}
            for familiar in [f[0] for f in familiares]:
                checkbox_name = f"{enfermedad}_{familiar}"
                enfermedad_dict[familiar] = checkbox_name in request.POST
            setattr(antecedentes, enfermedad, enfermedad_dict)

        antecedentes.save()

        # Enfermedades adicionales
        antecedentes.otras_enfermedades.all().delete()
        nombres_otros = request.POST.getlist("otra_nombre[]")
        for idx, nombre in enumerate(nombres_otros):
            if nombre.strip() == "":
                continue
            presencia = {}
            for familiar in [f[0] for f in familiares]:
                checkbox_name = f"otra_{familiar}_{idx}"
                presencia[familiar] = checkbox_name in request.POST

            OtraEnfermedad.objects.create(
                antecedente=antecedentes,
                nombre=nombre.strip(),
                presencia=presencia
            )

        return redirect('detalle_paciente', paciente_id=paciente.id)

    # 🔄 Construir una lista con todas las enfermedades + familiares + si están marcados
    enfermedades_estado = []
    for enfermedad in enfermedades_base:
        estado = getattr(antecedentes, enfermedad["name"], {})
        fila = {
            "name": enfermedad["name"],
            "label": enfermedad["label"],
            "familiares": [
                {"clave": f[0], "etiqueta": f[1], "checked": estado.get(f[0], False)}
                for f in familiares
            ]
        }
        enfermedades_estado.append(fila)

    return render(request, 'antecedentesPatologicos/formularioAntecedentes.html', {
        'paciente': paciente,
        'antecedentes': antecedentes,
        'enfermedades_estado': enfermedades_estado,
        'familiares': familiares,
    })
