# Lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ["Naty","Osvaldo","Lily","Ariel"]
print(nombres)

print("\n--- Mostramos un elemento en un indice especifico: ---")
print(nombres[0]) # Muestra el elemento en la posición indicada.
print(nombres[1])
print(nombres[3])
print(nombres[-1]) # Si no se sabe la longitud de la lista y se quiere conocer el último elemento, se indica el índice -1.
print(nombres[-2]) # Muestra el anteúltimo elemento.

print("\n--- Mostramos varios elementos en indices especificos: ---")
print(nombres[0:2]) # Muestra el índice 0 y 1. No el 2.
print(nombres[ :3]) # Muestra los elementos de la lista desde el primer elemento hasta el indice indicado sin incluirlo.
print(nombres[1: ]) # Muestra desde el índice indicado hasta el último elemento de la lista.

print("\n--- Modificamos elementos en indices especificos: ---")
nombres[2] = "Liliana" # Modificamos un elemento en el índice indicado.
nombres[0] = "Natalia"
print(nombres)
print("\n --- Iterando una lista con FOR: ---")
for nombre in nombres:
    print(nombre)
    break
else:
    print("Se acabaron los elementos de la lista.")

print("\n--- Para saber el tamaño del la lista (cantidad de elementos): ---")
print(len(nombres)) # A la funcion len debemos pasarle por parámetro la lista que queremos revisar.

print("\n--- Agregamos un elemento al final de la lista: ---")
nombres.append("Marcelo")
print(nombres)

print("\n--- Insertar un elemento en un indice especifico: ---")
nombres.insert(1, "Alberto")
nombres.insert(3, "Debora")
print(nombres)

print("\n--- Eliminamos elementos: ---")
nombres.remove("Alberto")
print(nombres)

print("\n--- Eliminamos el último elemento: ---")
nombres.pop()
print(nombres)

print("\n--- Eliminamos un indice especifico: ---")
del nombres[2] # La funcion del viene de DELETE (Eliminar)
print(nombres)

print("\n--- Eliminamos todos los elemento de la lista: ---")
nombres.clear()
print(nombres)

print("\n--- Eliminamos el último elemento: ---")
del nombres
print(nombres) # Nos va a dar error porque no tiene nada para imprimir.