from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def cifrar(request):
    return render(request,'cifrar.html')

def codificar(request):
    # mensaje = request.form["mensaje"]
    mensaje = request.POST.get("mensaje")
    rotaciones = int(request.POST.get("rotaciones"))
    # rotaciones = 13
    #Nota: también se puede importar a string y usar ascii_letters y ascii_uppercase
    alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁEÍÓÚ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha():
            codificado += letra
            continue
        valor_letra = ord(letra)
        # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
        alfabeto_a_usar = alfabeto
        limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        # Rotamos la letra
        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto

        # Convertimos el entero resultante a letra y lo concatenamos
        codificado += alfabeto_a_usar[posicion]
        context = {"resultadocifrado":codificado}
    # return render(request,"cifrar.html",{"resultadocifrado":codificado})
    return render(request,"cifrar.html",context)

def descifrar(request):
    return render(request)