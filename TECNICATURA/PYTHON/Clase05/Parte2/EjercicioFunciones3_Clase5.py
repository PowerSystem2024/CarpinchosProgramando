# Ejercicio 3: Funciones recursivas con factorial
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas.
# Puede ser cualquier valor positivo, por ejemplo: si se pasa el valor 3, se debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos, no imprime nada

def desplegarNum(numeros):
    if numeros >= 1:
        print(numeros)
        desplegarNum(numeros - 1)
    elif numeros == 0:
        return
    elif numeros <= 0:
        print('Valor ingresado negativo, intente de nuevo.')

numero = int(input("Ingrese un número entero positivo: "))
desplegarNum(numero)
