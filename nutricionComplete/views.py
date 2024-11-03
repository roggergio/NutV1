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
