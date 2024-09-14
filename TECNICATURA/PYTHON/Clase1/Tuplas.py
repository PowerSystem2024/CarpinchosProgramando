# lAS TUPLAS SON INMUTABLES (NO MODIFICABLES)

print("\n --- Elementos de la tupla: ---")
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)

print("\n --- Para ver el tamaño de nuestra tupla: ---")
print(len(cocina))

print("\n --- Para ver un elemento en un indice especifico: ---")
print(cocina[0])
print(cocina[-1]) # Nos muestra el último elemento.
print(cocina[-2]) # Nos muestra el anteúltimo elemento.

print("\n --- Acceder a un rango: ---")
print(cocina[0:2]) # El último elemento no se incluye. Solo muestra el 0 y 1

#Diferencia entre tupla y un dato tipo String
verduras = ("papa") # Si no tiene la coma despues del primer elemento, es un dato tipo String. No una tupla.

print("\n --- Recorremos los elemetos de la tupla: ---")
for cocinar in cocina:
    print(cocinar, end= " ") # print esta usando \n para saltos de líneas. Con end imprime en una sola línea

# Considerando que una tupla no puede ser modificada, se puede convertir la tupla en una lista y modificarla, despues se vuelve a convertir en tupla y tendriamos los elementos modificados. Pero no se recomienda el procedimiento ya que NO ES UNA BUENA PRACTICA.
print("\n\n --- Asi quedaria la tupla modificada: ---")
cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print(cocina)

print("\n --- Para eliminar una tupla: ---")
del cocina
print(cocina) # Nos va a dar error ya que no existiria una tupla que mostrar.