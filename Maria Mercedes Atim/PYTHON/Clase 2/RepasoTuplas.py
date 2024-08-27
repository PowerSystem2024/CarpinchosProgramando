# Las tuplas son inmutables y tambien pueden contener elementos de distinto tipo de datos.
# Podemos usar con tuplas las funciones: index(), count(), len()
# Las tuplas se pueden convertir en listas y viceversa.

tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola")
print("La tupla contiene elementos de distintos tipos de datos:\n",tupla)

print("\nVerificar si un elemento existe en la tupla: ")
print(4 in tupla) # Nos muestra un booleano.