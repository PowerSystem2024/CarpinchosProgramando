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