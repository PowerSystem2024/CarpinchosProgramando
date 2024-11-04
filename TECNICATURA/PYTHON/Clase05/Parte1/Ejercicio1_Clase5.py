# Ejercicio 1: No Repetir Caracteres
# Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caracteres.

cadena = input('Ingrese una cadena: ')
lista = []

for caracter in cadena:
    if caracter  not in lista:
        lista.append(caracter)
lista.sort()

print('La lista sin caracteres repetidos y ordenada queda de la siguiente manera: \n', lista)
