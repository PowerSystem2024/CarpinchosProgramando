# Concatenar listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2  # Concatenamos
print(lista3)

lista3.extend([7, 8, 9])    # '.extend' sirve para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))      # '.index' sirve para saber en que indice esta un elemento
# print(lista3.index(0))      # Nos da un error si ponemos un numero que no esta en la lista

# Como saber cuantos valores repetidos hay dentro de un lista
print(lista3.count(1))      # '.count' funcion. Le ingresamos el elemento del cual queremos saber cuantas veces esta repetido

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

# Metodos de ordenamiento
lista3.sort()  # '.sort' Siempre ordena de manera ascendente
print(lista3)

lista3.sort(reverse=True)      # Ordena de manera descendente
print(lista3)