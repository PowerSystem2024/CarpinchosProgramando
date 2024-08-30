# Diccionario: coleccion de datos. Compuesto por dos elementos
#              una LLAVE y un VALOR 
#               dict(key, value)
#              No tiene indice, como set. Puede modificarse.

# Estructura de diccionario
# ' llave ' : dato
# 'Maradona': 10   --> es un diccionario

diccionario = {
    'IDE': 'Integrated Develepoment Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
print(diccionario)

# Verifica la cantidad de elementos del diccionario.
print(len(diccionario)) 

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de acceder a un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)          # Nos muestra las llaves
    
# for termino, valor in diccionario:  | # No nos permite acceder al valor, sale error
#    print(termino, valor)


# Necesitamos una funcion para recorrer los valores del diccionario (items())
for termino, valor in diccionario.items():
    print(termino, valor)


# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)                  # .keys muestra solo las llaves
    
for valor in diccionario.values():  # .values muestra los valores
    print(valor)
    
    
# Comprobar la existencia de algun elemento
print('IDE' in diccionario)     # Nos da un booleano, pregunta si 'IDE' esta en 'diccionario'
print('IDE' not in diccionario)


# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# No nos deja agregar llaves duplicadas.


# Eliminar un elemento
diccionario.pop('SABD')  # Se elimina la llave  y el valor
print(diccionario)


# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario