# Ejercicio 2: Funciones - Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando los argumentos variables *args como parámetro de la función y
# regresar como resultado de la multiplicación de todos los valores pasados 
# como argumentos.
def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

numeros = input("Ingrese los valores que desea multiplicar (separados por espacios): ")
numeros = [int(x) for x in numeros.split(" ")]

resultado = multiplicar(*numeros)
print(f"El resultado de la multiplicación es: {resultado}")
