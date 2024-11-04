# Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor ingresado por el usuario.

lista = list(range(1,11))

print(f"\nLa lista original es: {lista}")

numero = int(input("\nIngrese un numero para multiplicar los elementos de la lista:\n "))

for num in lista:
    print(num*numero, end=" ")