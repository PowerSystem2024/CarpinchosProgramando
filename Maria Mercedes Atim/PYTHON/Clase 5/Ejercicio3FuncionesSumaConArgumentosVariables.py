# Crear una funcion para sumar los valores recibidos de tipo numericos utilizando argumentos variables *args como parámetros de la funcion y agregar como resultado la suma de todos los valores pasados como argumentos.
def sumar(*args):
    return sum(args)
print("El resultado de la suma es: ",sumar(1, 2, 3, 4))
print("El resultado de la suma es: ",sumar(10, 20, 30, 40, 50))
print(sumar())