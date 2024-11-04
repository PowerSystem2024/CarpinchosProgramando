# Pedir numeros y guardarlos en una lista. Cuando el usuario introduzca un numero 0, nuestro programa dejaria de insertar. Mostrar los numeros ordenados de menor a mayor.

lista = [] # Inicializamos una lista vacia.

while True:
    numero = int(input("Ingrese un numero. 0 para finalizar: ")) # Solicitamos un numero al usuario
    if numero == 0: # Si el numero ingresado es 0, el programa debe detenerse
        break
    lista.append(numero) # Se agrega a la lista el numero ingresado por el usuario

lista.sort() # Aqui ordenamos los numeros de forma ascendente.

print(f"\nLos numeros ingresados ordenados de menor a mayor son: {lista}")