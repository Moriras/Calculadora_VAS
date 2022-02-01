# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:19:37 2021

@author: VíctorAmellSerrano
"""
# BÁSICAS
import math

# FUNCIONES


def suma(x, y):
    print("Suma")
    resultado = x+y
    return resultado


def resta():
    print("Resta")
    n1 = (float(input("Introduce el primer número: ")))
    n2 = (float(input("Introduce el segundo número: ")))
    print(f"La resta de {n1} y {n2} es: {n1-n2}")


def multiplicacion():
    print("Multiplicación")
    n1 = (float(input("Introduce el primer número: ")))
    n2 = (float(input("Introduce el segundo número: ")))
    print(f"La multiplicación de {n1} y {n2} es: {n1*n2}")


def division():
    print("División")
    n1 = (float(input("Introduce el primer número (dividendo): ")))
    n2 = (float(input("Introduce el segundo número (divisor): ")))
    if(n2 == 0):
        print("No puedes dividir por 0")
    else:
        print(f"La división de {n1} y {n2} es: {n1/n2}")


def modulo():
    print("Módulo")
    n1 = (float(input("Introduce el primer número: ")))
    n2 = (float(input("Introduce el segundo número: ")))
    if(n2 == 0):
        print("No puedes dividir por 0")
    else:
        print(f"El resultado del módulo de {n1} y {n2} es: {n1%n2}")


def cociente():
    print("Cociente")
    n1 = (float(input("Introduce el primer número: ")))
    n2 = (float(input("Introduce el segundo número: ")))
    if(n2 == 0):
        print("No puedes dividir por 0")
    else:
        print(f"El resultado del cociente de {n1} y {n2} es: {n1//n2}")


def exponente():
    print("Exponente")
    n1 = (float(input("Introduce el primer número: ")))
    n2 = (float(input("Introduce el segundo número: ")))
    print(f"El resultado de {n1} elevado a {n2} es: {n1**n2}")


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
    print("Área de un triangulo")
    base = float(input("Introduce la base del triangulo en metros: "))
    altura = float(input("Introduce la altura del triangulo en metros: "))
    areaTriangulo = base * altura / 2
    print(
        f"El area de un triangulo de base {base} y altura {altura} es: {areaTriangulo}")


def areaCirculo():
    print("Área de un círculo")
    radio = float(input("Introduce el radio del circulo en metros: "))
    area = 3.14159242 * radio ** 2
    print(f"El area de un circulo de radio {radio}, es: {area}.")


def longitudCirculo():
    print("Longitud área círculo")
    radio = float(input("Introduce el radio del circulo en metros: "))
    longitud = 2 * math.pi * radio
    print(f"La longitud de un circulo de radio {radio}, es: {longitud}.")


def longitudAreaCirculo():
    print("Longitud área círculo")
    radio = float(input("Introduce el radio del circulo en metros: "))
    longitud = 2 * math.pi * radio
    print(f"La longitud de un circulo de radio {radio}, es: {longitud}.")


def salir():
    print("Salir")
    global salirBooleano
    salirBooleano = True


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
        n1 = (float(input("Introduce el primer número: ")))
        n2 = (float(input("Introduce el segundo número: ")))
        print("El resultado es:", suma(n1, n2))

    elif(seleccion == 2):
        resta()

    elif(seleccion == 3):
        multiplicacion()

    elif(seleccion == 4):
        division()

    elif(seleccion == 5):
        modulo()

    elif(seleccion == 6):
        cociente()

    elif(seleccion == 7):
        exponente()

    elif(seleccion == 8):
        numerosParesAreasCuadrados()

    elif(seleccion == 9):
        numerosParesAreasCirculos()

    elif(seleccion == 10):
        areaCuadrado()

    elif(seleccion == 11):
        areaRectangulo()

    elif(seleccion == 12):
        areaTriangulo()

    elif(seleccion == 13):
        areaCirculo()

    elif(seleccion == 14):
        longitudCirculo()

    elif(seleccion == 15):
        longitudAreaCirculo()

    elif(seleccion == 16):
        salir()

    else:
        print("Selección no válida")
