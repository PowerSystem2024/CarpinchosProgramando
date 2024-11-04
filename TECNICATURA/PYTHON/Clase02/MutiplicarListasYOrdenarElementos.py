# Para que una lista se multiplique repitiendo sus elementos
lista3 = [1, 2, 3, 1, 4, 5, 6, 1, 7, 8, 9, 1]
lista = [1, 2, 3] * 2
print("Se muestran los elementos multiplicados:",lista)
lista3 = lista3 * 2
print("\nSe muestran los elementos multiplicados de la lista 3:\n",lista3)

# Metodos de Ordenamiento
lista3.sort() # Muestra los elementos ordenados de manera ascendente.
print("\nLos elementos se muestran de forma ordenada y ascendente:\n",lista3)
lista3.sort(reverse=True)
print("\nLos elementos se muestran de forma ordenada y descendente:\n",lista3)