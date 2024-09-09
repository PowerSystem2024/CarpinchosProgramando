# Ejercicio: Valor dentro de un rango
# 1. Pedir al usuario un valor numérico.
# 2. Verificar si el valor ingresado se encuentre entre el rango 0 a 5.
# La fórmula es: <num> >= 0 and <num> <= 5

numero = int(input("Ingrese un número:"))
minimo = 0
maximo = 5

rango = (numero >= minimo and numero <= maximo)

if rango:
    print(f'El número {numero} está dentro del rango de números.')
else:
    print(f'El número {numero} no está dentro del rango de números.')

