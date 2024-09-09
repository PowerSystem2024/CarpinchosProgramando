# COLECCIONES EN PYTHON
# Listas -> Mutables (Se pueden editar)
# Conjunto de elementos (nombres, números, etc) de cualquier tipo de dato.

nombres = ['Ana', 'Lucas', 'Nelson', 'Lautaro']
print(nombres)
# print(nombres[0])
# print(nombres[1])
# print(nombres[3])
# print(nombres[-1])
# print(nombres[-2])
# Solo muestra el índice 0, 1 pero no el índice 2.
print(nombres[0:2]) 

# Ir del inicio de la lista al índice (sin incluirlo).
# Índices a mostrar: 0, 1, 2.
print(nombres[ :3])

# Desde el índice indicado hasta el final.
print(nombres[1: ])

# Modificar un valor dentro de la lista
nombres[2] = 'Mercedes'
nombres[0] = 'Paula'
print(nombres)

# Iterar una lista
# nombre es singular, la lista es plural
for nombre in nombres: 
    print(nombre)
else:
    print('Se acabaron los elementos de la lista.')

# Preguntar cuántos elementos que contiene la lista.
# El parámetro que está pidiendo 'len' es la lista 'nombres'
print(len(nombres))

# Agregar elementos a la lista.
nombres.append('Gabriel')
# nombres.append(1, 2, 3)
# nombres.append(True)
# nombres.append(10.45)
# nombres.append([4, 5])
# nombres.append(7)
print(nombres)

# Insertar un nuevo elemento en un índice específico
# insert necesirta si o si dos elementos, la posicion en la lista y el nombre del índice.
nombres.insert(1, 'Ana')
print(nombres)
nombres.insert(3, 'Omar')
print(nombres)

# Eliminar un elemento de la lista
nombres.remove('Paula')
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un índice específico
# del significa delete (eliminar)
del nombres[2]
print(nombres)

# Eliminar todos los elementos de la lista
nombres.clear()
print(nombres)

# Eliminar la lista
# El print muestra un error de que no existe
# del nombres
# print(nombres)

# Tuplas -> Inmutables (No se pueden editar)
# Para que sea una tupla y no un string, se necesita poner, aunque sea un elemento, una ','
# Definir una tupla.
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print(len(cocina))

# Acceder a un elemento, utilizar corchetes, no paréntesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])
print(cocina[-2])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ("papas",)

# Recorrer los elementos de la tupla
for cocinar in cocina:
    # Print utiliza \n para los saltos de línea
    # Para finalizar los saltos de línea hay que poner ", end=' '"
    print(cocinar)

# Modificar la tupla
# La única forma de modificar una tupla es realizando una conversión de tupla a lista, 
# modificar la lista y convertirla a tupla nuevamente.
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print(cocina)

# Eliminar una tupla
# del cocina
# print(cocina)

# Colección Tipo Set
# No tiene un orden y no permite almacenar elementos duplicados o repetidos, no se puede modificar pero se puede eliminar. Lo que quiere decir que no es mutable, pero tampoco inmutable.
# A la hora de imprimir, el orden del contenido es completamente aleatorio.

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
print(len(planetas))

# Revisar si un elemento existe dentro de set
# Es un tipo booleano (TRUE o FALSE). 
# Deben estar iguales, no puede tener una mayúscula o minúscula demás, ninguna letra menos o más.
print('Marte' in planetas)
print('Júpiter' in planetas)

# Agregar un elemento
# Para esto hay que utilizar la función 'add'
planetas.add('Tierra')
planetas.add('Tierra') # Este no afectaría porque no se pueden duplicar los elementos.
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe.
# En la función 'remove' ante un mal ingreso y inexistencia del elemento, da error.
planetas.remove('Júpiter')
print(planetas)

# Aquí se muestra el error
# planeta.remove('Urano')
# print(planetas)

# En la función 'discard' no se presenta ningún error.
planetas.discard('Tierra')
print(planetas)

planetas.discard('Urano')
print(planetas)

# Limpiar set o conjuto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
# del planetas
# print(planetas)

# DICCIONARIO DE PYTHON
# En lugar de tener una lista, hay una colección de datos ordenados de una manera particular.
# El diccionario está compuesto por dos elementos.
# 'Maradona' : 10
#  Llave  +  Valor asociado -> El conjunto de estas dos cosas es el diccionario.
# dict(key, value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
print(diccionario)

# Verificar los elementos del diccionario
print(len(diccionario))

# Acceder a un elemento del diccionario
# Para acceder a algún elemento del diccionario, hay que utilizar una llave (key)
# Se puede realizar mediante dos métodos
# Primer Método
print(diccionario['IDE'])

# Segundo Método
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos del diccionario
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Cómo recorrer los elementos 
# Solo las llaves
for termino in diccionario:
    print(termino)

# Recorrer el valor
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder al diccionario
# Solo las llaves
for termino in diccionario.keys():
    print(termino)

# Recorrer el valor
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algún elemento
print('IDE' in diccionario) # Devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
# del diccionario
# print(diccionario)

# REPASO DE LISTAS
# Concatenar listas
lista1 = [1, 1, 1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# Agregar varios elementos en la lista
lista3.extend([7, 8, 9])
print(lista3)

# En qué indicie esta el elemento elegido
print(lista3.index(5))
# print(lista3.index(0)) # Esto daría error por ser un elemento que no forma parte de la lista.

# Como saber cuántos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Cómo poner al revés la lista
lista3.reverse()
print(lista3)

# Cómo se multiplica la lista, repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
# sort(): Por default ordenará los elementos de manera ascendente
lista3.sort()
print(lista3)

# sort(reverse=True): Ordenará los elementos de manera descendente
lista3.sort(reverse=True)
print(lista3)

# REPASO DE TUPLAS
# ¿Qué se puede usar dentro de las tuplas?
#   Se pueden utilizar: index, count, len.
# Para modificar una tupla hay que convertirla en lista, modificar esa lista y volver a convertirla en tupla.
# Las tuplas pueden contener diferentes tipos de datos dentro de si.
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

# Se puede buscar un dato dentro de la tupla
# Acción booleana -> Su respuesta es tipo booleana
print(4 in tupla)

# REPASO DEL TIPO SET O CONJUNTO
# Los conmjuntos pueden tener distintos tipos de datos, pero los valores de los mismos deben ser únicos, no se pueden repetir.
# ¿Cómo definir un conjunto?
# Para poder inicializar un elemento vacío, solo se puede utilizar set, de otra forma, saltará error.
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)

conjunto1.add('Hola')
print(conjunto1)

# Preguntar si el número 3 NO está en el 'conjunto1'
# Acción booleana -> Su respuesta es tipo booleana
print(3 not in conjunto1) 

# Cómo hacer la igualdad de dos conjuntos
# Acción booleana -> Su respuesta es tipo booleana
print(conjunto1 == conjunto2)

# Operaciones en conjuntos
# RECORDAR -> No sigue una linea de índices, lo que imprima será en orden aleatorio
# La linea (|) une dos conjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto3)

# Intersección (&) -> El elemento que tienen en común dos (o más) conjuntos
conjunto3 = conjunto1 & conjunto2
print(conjunto3)

# Mostrar elementos que están en un conjunto pero no en el otro
conjunto3 = conjunto1 - conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

# Diferencia (^) -> Son los elementos que están en los dos conjuntos pero no están compartidos
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

# Cómo determinar si un conjunto es subconjunto de otro
# Acción booleana -> Su respuesta es tipo booleana
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))
print(conjunto2.issubset(conjunto3))

