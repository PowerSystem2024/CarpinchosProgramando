# Llenar una lista con los números del 1 al 50. Luego mostrar la lista con el bucle for. Los elementos deben mostrarse de la siguiente forma:
#1-2-3-4-5...-50

listaNumeros = list(range(1,51)) # creamos un rango de 50 numeros consecutivos y lo convertimos a lista. Se guarda en la lista ListaNumeros.

resultado = '' # Para mostrar el resultado en la forma especificada, creamos una variable resultado.

for i in range(len(listaNumeros)):
    if i < len(listaNumeros) - 1: # Mientras el numero final no sea 50, se le va a añadir a cada numero un guion.
        resultado += str(listaNumeros[i]) + '-'
    else: # para el numero 50 no se le agrega guion.
        resultado += str(listaNumeros[i])

print(resultado) # Se muestran los numeros de la lista.

'''
lista = list(range(1,51)) # Algoritmo eficaz
for i in lista:
    print(i, end='-')
'''