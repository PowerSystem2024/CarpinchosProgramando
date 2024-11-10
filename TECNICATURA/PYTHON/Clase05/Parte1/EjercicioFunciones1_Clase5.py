# Ejercicio 1: Funciones 
# Crear una función para sumar los valores recibidos de tipo numéricos, utilizando argumentos de variables *args como parámetro de la función y agregar como resultado la suma de todos los valores pasados como argumentos.

def suma(*args):
    return sum(args)

ingresoNum = input("Ingresar los números a sumar (Con espacios en medio de cada uno): \n")
numeros = map(float, ingresoNum.split())

resultado = suma(*numeros)

print(f'El resultado de la suma es: {resultado}')
