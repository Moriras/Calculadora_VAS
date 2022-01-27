# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:19:37 2021

@author: VíctorAmellSerrano
"""

print("¡Bienvenido a mi calculadora!\n")
print("¿Qué deseas realizar?\n")
print("1. Suma de 2 números")
print("2. Resta de 2 números")
print("3. Multiplicación de 2 números")
print("4. Dividir 2 números")
print("5. Módulo de 2 números")
print("6. Cociente de 2 números")
print("7. Exponente de 2 números ('x' elevado a 'y')")
print("8. Salir")

seleccion=(int(input("Selecciona: ")))

if(seleccion==1):
    print ("Suma")
    n1=(float(input("Introduce el primer número: ")))
    n2=(float(input("Introduce el segundo número: ")))
    print(f"La suma de {n1} y {n2} es: {n1+n2}")

elif(seleccion==2):
    print ("Resta")
    n1=(float(input("Introduce el primer número: ")))
    n2=(float(input("Introduce el segundo número: ")))
    print(f"La resta de {n1} y {n2} es: {n1-n2}")

elif(seleccion==3):
    print ("Multiplicación")
    n1=(float(input("Introduce el primer número: ")))
    n2=(float(input("Introduce el segundo número: ")))
    print(f"La multiplicación de {n1} y {n2} es: {n1*n2}")

elif(seleccion==4):
    print ("División")
    n1=(float(input("Introduce el primer número (dividendo): ")))
    n2=(float(input("Introduce el segundo número (divisor): ")))
    if(n2==0):
        print("No puedes dividir por 0")
    else:
        print(f"La división de {n1} y {n2} es: {n1/n2}")

elif(seleccion==5):
    print ("Módulo")
    n1=(float(input("Introduce el primer número: ")))
    n2=(float(input("Introduce el segundo número: ")))
    if(n2==0):
        print("No puedes dividir por 0")
    else:
        print(f"El resultado del módulo de {n1} y {n2} es: {n1%n2}")
    
elif(seleccion==6):
    print ("Cociente")
    n1=(float(input("Introduce el primer número: ")))
    n2=(float(input("Introduce el segundo número: ")))
    if(n2==0):
        print("No puedes dividir por 0")
    else:
        print(f"El resultado del cociente de {n1} y {n2} es: {n1//n2}")
    
elif(seleccion==7):
    print ("Exponente")
    n1=(float(input("Introduce el primer número: ")))
    n2=(float(input("Introduce el segundo número: ")))
    print(f"El resultado de {n1} elevado a {n2} es: {n1**n2}")

elif(seleccion==8):
    print ("Salir")


else:
    print ("Selección no válida")