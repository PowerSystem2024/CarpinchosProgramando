# Creamos listas para concatenarlas:
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
print(f"La lista 1 contiene: {lista1} y la lista 2 contiene {lista2}")
lista3 = lista1 + lista2
print("Las dos listas concatenadas se muestran asi: ",lista3)

print("\nUsamos la funcion extend para agregar mas elementos a la lista: ")
lista3.extend([7, 8, 9, 1])
print(lista3)

print("\nUsamos la funcion index() para saber en que posicion se encuentra el elemento especificado: ")
print(lista3.index(5)) # Le pasamos por parámetro el elemento para averiguar el índice. Si el elemento no existe, nos da error.

print("\nVerificamos cuantas veces se repite en la lista el valor especificado: ")
print(lista3.count(1)) # Cuenta cuantos elementos iguales hay en la lista.

print("\nMostramos los elementos de la lista al reves: ")
lista3.reverse() # Esto modifica la lista original y revierte el orden.
print(lista3)
print(lista3[::-1]) # El slicing lista[inicio:fin:paso] permite manipular la lista de forma versatil sin modificar e original.