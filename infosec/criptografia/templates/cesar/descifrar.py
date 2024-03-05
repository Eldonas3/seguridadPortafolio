def decodificar(mensaje, rotaciones):
    #Nota: también se puede importar a string y usar ascii_letters y ascii_uppercase
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    decodificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            decodificado += letra
            continue
        valor_letra = ord(letra)
        # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
        alfabeto_a_usar = alfabeto
        limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        # Rotamos la letra, ahora hacia la izquierda
        posicion = (valor_letra - limite - rotaciones) % longitud_alfabeto

        # Convertimos el entero resultante a letra y lo concatenamos
        decodificado += alfabeto_a_usar[posicion]
    return decodificado