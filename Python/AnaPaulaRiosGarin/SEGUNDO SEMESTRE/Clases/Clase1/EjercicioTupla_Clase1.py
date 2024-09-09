# Ejercicio Tupla
# Dada la siguiente tupla:
#   tupla = (13, 1, 8, 3, 2, 5, 8) -> Definir la tupla
# Crear una lista que incluya únicamente los números menores a 5.
# Imprimir por consola [1, 2, 3]

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)
