#                       --- Video 1 ---

# Definimos una tupla | usamos parentesis ()

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)


# Para saber la cantidad de elementos que tiene una tupla
print(len(cocina))


# Como acceder a un elemento de la tupla. Utilizamos corchetes, no parentesis

print(cocina[0])
print(cocina[1])
print(cocina[2])


# Mostrar de manera inversa

print(cocina[-1])       # Nos muestra el ultimo elemento
print(cocina[-2])
print(cocina[-3])


# Acceder a un rango

print(cocina[0:1])
print(cocina[0:2])


# Ejemplo de una tupla con un solo elemento

verdura = ('papa')      # Esto es una cadena (string, str)
verdura = ('papa',)     # con la coma es una tupla



#__________________________________________________________________________
#                           --- Video 2 ---

# Recorremos los elementos de una tupla

for cocinar in cocina:

    print(cocinar, end=' ')      # Print esta usando la barra diagonal inversa n para salto de lineas
                                 # Con el end= ' ', para eliminar los saltos de linea


# Para modificar una tupla debemos hacer una conversion de tupla a lista, y de lista a tupla nuevamente

cocinaLista = list(cocina)      # Conversion de tupla a lista
cocinaLista[0] = 'Plato'        # Modificamos el elemento
cocina = tuple(cocinaLista)     # Conversion de lista a tupla nuevamente
print('\n', cocina)

# No es una buena practica...



# Eliminar una tupla
del cocina