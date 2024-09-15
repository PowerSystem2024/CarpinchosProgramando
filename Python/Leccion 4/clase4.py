 Clase4
# eliminar duplicados de una lista, escribir un programa donde tenga una lista y que a continuación elimine los elementos duplicados, por ultimo mostrar la lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]

listaSinDuplicados = list(set(lista))

print(listaSinDuplicados)

# escribir un programa que tenga dos listas y que a continuación cree las siguientes listas (en las que no debe haber repetición)

# lista con las palabras que aparecen en las listas
# lista de palabras que aparecen en la primer lista pero no en la segunda
# lista de palabras que aparecen en la segunda lista pero no en la primera
# lista de palabras que aparecen en ambas listas

lista1 = {"hola", "como", "estas", "hello", "word"}
lista2 = {"chau", "nos", "vemos", "hello", "word"}

print(lista1)
print(lista2)

listaPrimera = lista1 - lista2
print(listaPrimera)

listaSegunda = lista2 - lista1
print(listaSegunda)

listaConjuncion = lista1 | lista2
print(listaConjuncion)
# escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos:

# nombre: aragon  
# clase: guerrero
# raza: dunadan del norte

# nombre: gandalf  
# clase: mago
# raza: istar

# nombre: legolas  
# clase: arquero
# raza: elfo sindar

personajes = [] # Creamos una lista vacia
P = {'Nombre' : 'Aragorn', 'Clase' : 'Guerrero', 'Raza' : 'Dunadan del Norte'}
personajes.append(P) # agregamos a la lista a un personaje
P = {'Nombre' : 'Gandalf', 'Clase': 'Mago', ' Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase' : 'Arquero', 'Raza' : 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': 'Gimli', 'Clase' : 'Erebor', 'Raza' : 'Enano'}
personajes.append(P)
P = {'Nombre': 'Froddo', 'Clase' : 'Boggin', 'Raza' : 'Hobbit'}
personajes.append(P)
P = {'Nombre': 'Sauron', 'Clase' : 'Maiar', 'Raza' : 'Aule'}
personajes.append(P)
print(personajes)


# obtener la raiz cuadrada de un numero positivo

import math

numero = int(input("ingrese un numero positivo: "))

#if (numero < 0):
#    print("el numero debe ser mayor a cero")
#else:
#    print(f'la raiz del numero {numero} es {math.sqrt(numero)}')

while numero < 0:

    print('error, el numero debe ser positivo')
    numero = int(input("ingrese un numero positivo: "))

print(f'la raiz del numero {numero} es {math.sqrt(numero)}')

# obtener la raiz cuadrada de un numero positivo

import math

numero = int(input("ingrese un numero positivo: "))

#if (numero < 0):
#    print("el numero debe ser mayor a cero")
#else:
#    print(f'la raiz del numero {numero} es {math.sqrt(numero)}')

while numero < 0:

    print('error, el numero debe ser positivo')
    numero = int(input("ingrese un numero positivo: "))

print(f'la raiz del numero {numero} es {math.sqrt(numero)}')
# llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor ingresado por el usuario

numeros = [i for i in range(1, 11)]
numerosMultiplicados = []

numeroMultiplicador = int(input("ingrese un numero para multiplicar los elementos de la lista "))

for i in numeros:
    numerosMultiplicados.append(i * numeroMultiplicador)

print(numerosMultiplicados)
# pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0, nuestro programa dejaria de insertar, por ultimo, mostrar los numeros de menor a mayor

lista = []

while (True):

    numero = int(input("ingrese un numero, para terminar el programa ingrese 0: "))

    if (numero != 0):
        lista.append(numero)
    else:
        break


print(f'lista original: {lista}')

lista.sort()

print(f'lista ordenada: {lista}')

# hacer un programa que sume numero pares dentro de un rango, por ejemplo, umar los numeros pares del 2 al 30

suma = 0

numeroMin = int(input("ingrese el numero minimo del rango "))
numeroMax = int(input("ingrese el numero maximo del rango "))

if (numeroMax < numeroMin):
    print("los numeros no concuerdan, por favor, intente de nuevo")
else:
    for i in range(numeroMin, numeroMax + 1):
        if (i % 2 == 0):
            suma += i
    print(f"la suma de los numeros pares entre {numeroMin} y {numeroMax} es {suma}")


# calcular el factorial de un numero positivo

def factorial(numero):
    if numero == 0:
        return 0
    elif(numero == 1):
        return 1
    else:
        return numero * factorial(numero -1)

numero = int(input("ingrese un numero para calcular el factorial "))

print(f'el factorial de {numero} es {factorial(numero)}')

def mi_funcion():
    print('saludos a todos mis compañeros')

mi_funcion()

# hacer un programa que puda un numero por teclado y guarde en la lista su tabal de multiplicar hasta el 10

def tablaMultiplicar(numero):
    listaMultiplicar = []
    for i in range(0, 11):
        listaMultiplicar.append(numero * i)
    return listaMultiplicar

numero = int(input("ingrese un numero "))

print(f"la tabla de multiplicar del numero {numero} es {tablaMultiplicar(numero)}")



# realizar un juego para adivinar un numero, para ello se debe generar un numero aleatorio entre 1 y 100, luego ir pidiendo numeros indicando si es mayor o menor, cuando se adivine el numero
# mostrar la cantidad de usuarios

import random

def adivinanzas():

    numeroAdivinanza = random.randint(1, 100)

    contadorIntentos = 0;

    print("vamos a jugar a las adivinanzas")

    while True:

        numero = int(input("ingresa un numero "))


        if(numero < numeroAdivinanza):
            print("el numero que estas buscando es mayor al ingresado")
            contadorIntentos += 1
        elif (numero > numeroAdivinanza):
            print("el numero que estas buscando es menor al ingresado")
            contadorIntentos += 1
        elif(numero == numeroAdivinanza):
            print(f'GANASTE, el numero que buscabas es el {numero}')
            break

    print(f'cantidad de intentos: {contadorIntentos + 1}')

adivinanzas()

# hacer un programa que simule un cajero automatico con un saldo inicial de 1000 y tendra el siguiente menu de opciones

# ingresar dinero a la cuenta
# retirar dinero de la cuenta
# mostrar dinero disponible
# salir
def cajero():
    saldo = 1000  # Inicializar el saldo una sola vez

    print('Bienvenido, seleccione una de las siguientes opciones: ')

    while True:
        opcion = int(input(""" \n
                        para ingresar dinero a su cuenta, seleccione 1 \n
                        para retirar dinero de su cuenta, seleccione 2 \n 
                        para mostrar el saldo disponible en su cuenta, seleccione 3 \n 
                        para salir ingrese 4
                        """))

        if opcion == 1:

            print(f'Su saldo actual es de {saldo}')

            monto = int(input("Ingrese la cantidad a depositar en su cuenta: "))
            saldo += monto

            print(f'Su saldo actual es de {saldo}')

        elif opcion == 2:

            print(f'Su saldo actual es de {saldo}')

            monto = int(input("Ingrese la cantidad a retirar de su cuenta: "))

            if monto > saldo:
                print("No tiene el saldo  suficiente para realizar esta operación.")
            else:
                saldo -= monto
                print(f'Su saldo actual es de {saldo}')

        elif opcion == 3:

            print(f'Su saldo actual es de {saldo}')

        elif opcion == 4:

            print("Gracias por usar nuestros servicios")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")∫



# hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacios en blanco, y un contador de los caracteres de la frase

# Solicitar al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

# Eliminar los espacios en blanco de la frase
frase_sin_espacios = frase.replace(" ", "")

# Contar los caracteres de la frase sin espacios
contador_caracteres = len(frase_sin_espacios)

# Mostrar la frase sin espacios y el contador de caracteres
print("Frase sin espacios:", frase_sin_espacios)
print("Número de caracteres:", contador_caracteres)

