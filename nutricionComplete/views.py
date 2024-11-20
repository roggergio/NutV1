from django.shortcuts import render
def login(request):
    return render(request, 'login.html')
def aside_1(request):
    return render(request, 'aside_1.html')
def aside_2(request):
    return render(request, 'aside_2.html')
def navBar(request):
    return render(request, 'navBar.html')
def price(request):
    return render(request, 'price.html')

def pacientesList(request):
    return render(request, 'pacientesList.html')

def home(request):
    return render(request, 'home.html')
def datos_generales(request):
    return render(request, 'datosPaciente.html')

def consultar(request):
    return render(request, 'baseConsultar.html')

def equivalentes(request):
    return render(request, 'equivalentes.html')

def macronutrientes(request):
    return render(request, 'macronutrientes.html')
def enfermedades(request):
    return render(request, 'enfermedades.html')
def habitos(request):
    return render(request, 'habitos.html')

def quimica_sanguinea(request):
    return render(request, 'quimica_sanguinea.html')

def alergiasYAdicciones(request):
    return render(request, 'alergiasYAdicciones.html')

def bioquimicosPaciente(request):
    return render(request, 'bioquimicosPaciente.html')
def antecedentesPatologicos(request):
    return render(request, 'antecedentesPatologicos.html')
def antropometria(request):
    return render(request, 'antropometria.html')
<<<<<<< HEAD
def medicamentos(request):
    return render(request, 'medicamentos.html')
def r24(request):
    return render(request, 'r24.html')
def energiaActividad(request):
    return render(request, 'energiaActividad.html')
=======
>>>>>>> 8ad416f37ae1d4a1cf2d2ecb72d4cd20a34c7408
