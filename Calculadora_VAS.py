# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:19:37 2021

@author: VíctorAmellSerrano
"""
# BÁSICAS
import math

# FUNCIONES
linea 11 cambio B

def suma(x, y):
    return x+y


def resta(x, y):
    return x-y


def multiplicacion(x, y):
    return x*y


def division(x, y):
    if(n2 == 0):
        print("No puedes dividir por 0")
    else:
        print(f"La división de {n1} y {n2} es: {n1/n2}")


def modulo(x, y):
    if(n2 == 0):
        print("No puedes dividir por 0")
    else:
        print(f"El resultado del módulo de {n1} y {n2} es: {n1%n2}")


def cociente(x, y):
    if(n2 == 0):
        print("No puedes dividir por 0")
    else:
        print(f"El resultado del cociente de {n1} y {n2} es: {n1//n2}")


def exponente(x, y):
    return x**y


def numerosParesAreasCuadrados():
    contador = 0
    numeroDePares = int(input("Numero de pares solicitado: "))
    for l in range(1, numeroDePares*2+1):
        if(l % 2 == 0):
            contador += 1
            print(f"El área del cuadrado Nº {contador} de lado {l}, es {l*l}")


def numerosParesAreasCirculos():
    contador = 0
    numeroDePares = int(input("Numero de pares solicitado: "))
    for l in range(1, numeroDePares*2+1):
        if(l % 2 == 0):
            contador += 1
            print(
                f"El área del círculo Nº {contador} de radio {l}, es {math.pi*l**2}")


def areaCuadrado():
    print("Área de un cuadrado")
    cuadrado = float(input("Introduce un lado del cuadrado en metros: "))
    areaCuadrado = cuadrado * cuadrado
    print(
        f"El area de un cuadrado con los lados de {cuadrado}, es:", areaCuadrado)


def areaRectangulo():
    print("Área de un rectángulo")
    baseRectangulo = (
        int(input("Introduce la base del rectangulo en metros: ")))
    alturaRectangulo = (
        int(input("Introduce la altura del rectangulo en metros: ")))
    areaRectangulo = baseRectangulo * alturaRectangulo
    print(f"El area de un rectángulo con base {baseRectangulo} y altura \
     {alturaRectangulo} es: {areaRectangulo}")


def areaTriangulo():
    areaTriangulo = base * altura / 2
    return areaTriangulo


def areaCirculo(r):
    area = 3.14159242 * radio ** 2
    return area


def longitudCirculo(r):
    longitud = 2 * math.pi * radio
    return longitud

# Esta opción no es la mas correcta.
# def longitudAreaCirculo(r):
#     print("Longitud y área del círculo")
#     area = areaCirculo(r)
#     longitud = longitudCirculo(r)
#     return area, longitud


def longitudAreaCirculo(r):
    print("Longitud y área del círculo")
    return areaCirculo(r), longitudCirculo(r)


def salir():
    print("Salir")
    global salirBooleano
    salirBooleano = True

sumaLambda = lambda x,y:x+y


# VARIABLES
seleccion = int()
salirBooleano = False

print("¡Bienvenido a mi calculadora!\n")

while not (salirBooleano == True):
    print("==================================\n")
    print("¿Qué deseas realizar?\n")
    print("1. Suma de 2 números")
    print("2. Resta de 2 números")
    print("3. Multiplicación de 2 números")
    print("4. Dividir 2 números")
    print("5. Módulo de 2 números")
    print("6. Cociente de 2 números")
    print("7. Exponente de 2 números ('x' elevado a 'y')")
    print("8. Área de los cuadrados pares de x números")
    print("9. Área de los círculos de radio par de x números")
    print("10. Área de un cuadrado")
    print("11. Área de un rectángulo")
    print("12. Área de un triangulo")
    print("13. Área de un círculo")
    print("14. Longitud de un círculo")
    print("15. Area y longitud de un círculo")
    print("16. Salir")
    seleccion = (int(input("Selecciona: ")))

    if(seleccion == 1):
        print("Suma")
        n1 = (float(input("Introduce el primer número: ")))
        n2 = (float(input("Introduce el segundo número: ")))
        print(f"La suma de {n1} + {n2} es:", sumaLambda(n1, n2))
        # print(f"La suma de {n1} + {n2} es:", suma(n1, n2))

    elif(seleccion == 2):
        print("Resta")
        n1 = (float(input("Introduce el primer número: ")))
        n2 = (float(input("Introduce el segundo número: ")))
        print(f"La resta de {n1} y {n2} es: {resta(n1, n2)}")

    elif(seleccion == 3):
        print("Multiplicación")
        n1 = (float(input("Introduce el primer número: ")))
        n2 = (float(input("Introduce el segundo número: ")))
        print(f"La multiplicación de {n1} y {n2} es: {multiplicacion(n1,n2)}")

    elif(seleccion == 4):
        print("División")
        n1 = (float(input("Introduce el primer número (dividendo): ")))
        n2 = (float(input("Introduce el segundo número (divisor): ")))
        division(n1, n2)

    elif(seleccion == 5):
        print("Módulo")
        n1 = (float(input("Introduce el primer número: ")))
        n2 = (float(input("Introduce el segundo número: ")))
        modulo(n1, n2)

    elif(seleccion == 6):
        print("Cociente")
        n1 = (float(input("Introduce el primer número: ")))
        n2 = (float(input("Introduce el segundo número: ")))
        cociente(n1, n2)

    elif(seleccion == 7):
        print("Exponente")
        n1 = (float(input("Introduce el primer número: ")))
        n2 = (float(input("Introduce el segundo número: ")))
        print(f"El resultado de {n1} elevado a {n2} es: {exponente(n1,n2)}")

    elif(seleccion == 8):
        numerosParesAreasCuadrados()

    elif(seleccion == 9):
        numerosParesAreasCirculos()

    elif(seleccion == 10):
        areaCuadrado()

    elif(seleccion == 11):
        areaRectangulo()

    elif(seleccion == 12):
        print("Área de un triangulo")
        base = float(input("Introduce la base del triangulo en metros: "))
        altura = float(input("Introduce la altura del triangulo en metros: "))
        areaTriangulo()
        print(f"El area de un triangulo de base {base} y altura {altura} es: \
                {areaTriangulo}")

    elif(seleccion == 13):
        print("Área de un círculo")
        radio = float(input("Introduce el radio del circulo en metros: "))
        print(f"El area de un circulo de radio {radio}, es: \
              {areaCirculo(radio)}.")

    elif(seleccion == 14):
        print("Longitud área círculo")
        radio = float(input("Introduce el radio del circulo en metros: "))
        long = longitudCirculo(radio)
        print(f"La longitud de un circulo de radio {radio}, es: {long}.")

    elif(seleccion == 15):
        radio = float(input("Introduce el radio del circulo en metros: "))
        area, longitud = longitudAreaCirculo(radio)
        print(f"El circulo de radio {radio}, tiene un area de {area} y \
              una longitud de {longitud}.")
        # Tambien podria ser
        # resultado=longitudAreaCirculo(radio)
        # print(f"El circulo de radio {radio}, tiene un area de {resultado[0]} y una longitud de {resultado[1]}.")

    elif(seleccion == 16):
        salir()

    else:
        print("Selección no válida")
