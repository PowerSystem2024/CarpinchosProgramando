#lista = wanda, nico,paula, mercedes, mariana, nelson

nombres =["Wanda", "Nico","Paula","Mercedes","Mariana","Nelson"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[4])
print(nombres[5])
print(nombres[-2])
print(nombres[0:2]) #Solo muestrael el indice 0 , 1 pero no el 2



print (nombres[ :4])
   # Al dejar el espacio vacio damos a entender que queremos solo las 
   # 4 primeras posiciones, por lo tanto se muestra hasta el indice

print (nombres[ 2: ])
   # Al dejar el espacio vacio damos a entender que queremos desde el
   # indice 2 "Paula" hasta el final 

nombres[3] = "Mercedes"
nombres[0] = "Wanda"
print(nombres)

# Iterar una lista
for nombre in nombres:
 print(nombre)
   # Para mostrar los nombres por separado

else: 
 print("Se acabaron los integrantes del grupo carpinchos programando")

# Fin de Listas Parte 2

#  Listas Parte 3



print(len(nombres)) 
   # "len" nos indica la cantidad de elementos que tiene una lista
   # Como parametro le pasamos la lista

nombres.append("Fernando") 
   # "append" sirve paraagregar elementos a una lista 

print(nombres)
   # El elemento se ingresa al final de la lista 

nombres.insert(1,"Javier") 
   # Esta funcion se ejecuta con un entero + el elemento
   # que queremos ingresar a nuestra lista

print(nombres)
   # Corre los otros elementos a la derecha

nombres.insert(3,"Victoria") 
   # Otro ejemplo

print(nombres)
   # Se puede apreciar que "Mercedes" que estaba en la posicion 3
   # y ahora paso a estar en ña posicion 4 agregando a "Victoria"
   # en la posicion 3

nombres.remove("Victoria")
   # Esta funcion Remueve el elemento de la lista que elijamos

print(nombres)

nombres.pop()
   # Esta funcion usado de esta manera remueve el ultimo elemento 
   # de la lista

print(nombres)

del nombres [1]
   # Elimina una posicion "del" significa "delete "(eliminar)

print(nombres)
   # Se elimino el nombre "Javier"

nombres.clear()
   # Elimina/limpia todos los elementos de la lista 

print(nombres)
   # Se borro todo el contenido de "nombres"

del nombres 
   # Eliminamos "nombres"

print(nombres)
   #Salta error de que no esta definida "nombres"
   
# Fin de Listas Parte 3

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3 

print() #Salto de linea 
print("Rango de numeros entre 0 y 10 divisibles entre 3")
print() #Salto de linea 

for i in range(1,11):
 if i % 3 == 0:
  print(i)

# Fin Ejercicio 1

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimelos 

print() #Salto de linea 
print("Rango con valores inicio = 2 y fin = 6")
print() #Salto de linea 

for i in range(2,7):
 print(i)

# Fin Ejercicio 2

# Ejercicio 3

print() #Salto de linea 
print("Rango con valores de inicio = 3, fin = 10, incremento = 2") 
print() #Salto de linea 

for i in range(3,11,2):
 print(i)

print() #Salto de linea 

 # Fin Ejercicio 3
#--------------------------------------------

 # Definimos una tupla 

cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))

# Para acceder a un elemento usamos corchetes, no parentesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina [0:2])

   # Muestra solo "Cuchara" y "cuchillo"  porque muestra el 
   # elemento "0" y "1", al 2 no llega 

# Ejemplo de cadena 
verduras = ("papa")

print(verduras)

# Diferencia entre cadena y tupla al imprimir 
# ('cuchara',) = tupla
# papa = cadena 

verduras = ("papa",)
# Pasa a ser tupla, porque necesita aunque sea de un elemento: la coma
# De lo contrario, solo pasaria a ser un tipo str cadena

print(verduras)

#Recorremos los elementos de la tupla 
for cocinar in cocina:
 print(cocinar) # print esta usando /n para saltos de lineas 

for cocinar in cocina:
  print(cocinar, end=" ") # Print finaliza los saltos de linea al usar: (end=" ")


#  cocina[0] = "plato"
#   print(cocina) 

# Salta error porque en las tuplas no se pueden modificar los elementos

cocinarLista = list(cocina)
cocinarLista[0] = "Plato"
cocina = tuple(cocinarLista)
print("\n",cocina) # Print reanuda los saltos de linea con ("\n",)

#NO ES BUENO HACER ESTA CONVERSION DE TUPLA A LISTA Y DE LISTA A TUPLA

# No se puede utilizar en tuplas:

# .append 
# .insert
# .remove


   # del cocina
# Elimina la tupla


# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5
# e imprimir por consola [1,3,2]
# Creamos una lista que solo incluya los números menores a 5
lista = []

for num in tupla:
     if num < 5:
          lista.append(num)


# Imprimimos la lista 
print(lista)

# del cocina #

#Clase 2
# tipo set
planetas = {'Marte', 'Jupiter', 'Venus'}

# revisar si un elemento existe dentro de set
print('Jupiter' in planetas)  # usamos la función in para verificar existencia

# agregar un elemento
planetas.add('Tierra')  # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Jupiter")  # 'Jupiter' debe estar en mayúscula
# Esta función no nos presenta ningún error
planetas.discard("Tierra")  # discard no arroja error si el elemento no existe
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)  # Esto imprimirá un set vacío

# Eliminar set o conjunto
del planetas


print(planetas) 

#"Messi" :  10
# UNA LLAVE {} Y UN DICCIONARIO ESTA COMPUESTO POR DOS ELEMENTOS
# Una llave y un valor

diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programación Orientada a Objetos",
    "SABD":"Sistema de administracion de basde de datos"
}

print(diccionario)

#VERIFICAR LA CANTIDAD DE ELEMENTOS DEL DICCIONARIO
print(len(diccionario))
print(diccionario)

#acceder a un diccionario con la llave
print(diccionario["IDE"])
#otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))
#Modificamos elementos

diccionario["IDE"] = "Entorno desarrollo integrado"
print(diccionario)


#Concatenar listas

lista1 = [1, 1, 2, 3]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9]) #agregar varios elementos
print(lista3)

print(lista3.index(5)) #donde ubica el valor en el index

#Como saber cuantos valores repetidos hay en la lista
print(lista3.count(1))

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

#Metodos de ordenamiento
lista3.sort() #Ordena de manera ascendente
print(lista3)
lista3.sort(reverse=True) #Ordena descendente
print(lista3)

#Repaso Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') #Puede tener diferentes tipos de datos
print(tupla) #bool si existe
#Lo que podemos usar en tuplas: index, count, lenght

print(4 in tupla)
#Otras funciones de las listas (tambien llamadas arreglos o vectores)

#Listas dentro de listas
nombres = ['Ariel', 'Naty']
nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

print("Rango de 0 a 10 con numeros diisibles entre 3")
for i in range (11):
    if i % 3 == 0:
       print(i)

print("Rango con valores de inicio = 2 y fin = 6")
rango = range(2, 7)
for i in rango:
    print(i)

print("Rango con valores de inicio = 3, fin = 10, incremento = 2")
for i in range(3, 11, 2):
    print(i)

# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")

print(len(cocina))
# Mostrar el primer elemento
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])
# Acceder a un rango
print(cocina[0:1])
# Ejemplo
verduras = ("papa",)
# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=" ")

cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

#del cocina
#print(cocina)

tuple_data = (13, 1, 8, 3, 2, 5, 8)
list_data = []
for elemento in tuple_data:
    if elemento < 5:
        list_data.append(elemento)
print(list_data)

conjunto2 = set()
conjunto1 = {"bye", }
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1)

# Como hacer igualdad entre dos conjuntos
print(conjunto1 == conjunto2)

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2  # La línea une los dos conjuntos
print(conjunto3)
conjunto3 = conjunto1 & conjunto2  # Qué elementos tienen en común
print(conjunto3)
conjunto3 = conjunto1 - conjunto2  # Asigna el valor que está en conjunto1 pero no en conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)
conjunto3 = conjunto1 ^ conjunto2  # Elementos que no comparten
print(conjunto3)

# Preguntamos si un conjunto es subconjunto de otro
print(conjunto2.issubset(conjunto3))
print(conjunto1.issubset(conjunto3))

# Superset
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))

# Conjuntos disconexos
print(conjunto1.isdisjoint(conjunto2))

# Convertir un conjunto a inmutable
conjunto1 = frozenset(conjunto1)

# REPASO DICCIONARIO
# del (diccionarioNuevo["Azul"])
# print(diccionarioNuevo)

# Diccionarios con diferentes tipos de datos
diccionario2 = {
    "Mercedes": {"Edad": 40, "Altura": 1.83},
    "Miguel": [45, 1.85],
    "Wanda": [35, 1.67]
}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 millones", "Posición": "Extremo derecho"},
    11: {"Nombre": "Ángel Di María", "Edad": 34, "Altura": 1.80, "Precio": "12 millones", "Posición": "Extremo derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 millones", "Posición": "Media Punta"},
    19: {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "50 millones", "Posición": "Defensa central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 millones", "Posición": "Arquero"},
    7: {"Nombre": "Rodrigo De Paul", "Edad": 28, "Altura": 1.80, "Precio": "40 millones", "Posición": "Mediocampista"},
    3: {"Nombre": "Nicolás Tagliafico", "Edad": 30, "Altura": 1.72, "Precio": "9 millones", "Posición": "Lateral izquierdo"},
    22: {"Nombre": "Lautaro Martínez", "Edad": 25, "Altura": 1.74, "Precio": "75 millones", "Posición": "Delantero centro"},
    8: {"Nombre": "Marcos Acuña", "Edad": 31, "Altura": 1.72, "Precio": "12 millones", "Posición": "Lateral izquierdo"}
}

#for llave, valor in seleccionArgentina.items()
#    print(llave, valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end)
print(len(seleccionArgentina))

#Pilas usando listas 
pila = [1, 2, 3]

#agregar elementos a la pila por el final 
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #quita el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elemento{elementoBorrado}")
print(f"La fila ahora quedo asi ")

#Colas con listas 
#Estructuras de datos tipo fifo( first input /first output)

cola = ["Ariel", "Nicolas", "Fernando", "Mercedes"]
cola.append("Wanda")
cola.append("Miguel")
print (cola)

#Sacamos elementos de la cola 
seRetira = cola.pop(0)
print(f"Atendido{seRetira}")
print (cola)

# Clase4
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

# hacer un programa que puda un numero por teclado y guarde en la lista su tabla de multiplicar hasta el 10

tablaDeMultiplicar = []

numero = int(input("Ingrese un numero para crear su tabla de multiplicar: "))

for i in range(0, 11):
    tablaDeMultiplicar.append(numero * i)
    print(f"{numero} x {i} = {tablaDeMultiplicar[-i]}")

print(f"\nLa lista completa quedaría así: {tablaDeMultiplicar}")



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

def frase():

    frase = input("ingrese una frase: ")

    fraseSinEspacios = frase.replace(" ","")

    contador = len(fraseSinEspacios)

    print(f'la frase sin espacios es {fraseSinEspacios}')
    print (f'la frase tiene {contador} caracteres')


frase()




