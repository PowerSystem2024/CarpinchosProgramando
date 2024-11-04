# Funcion con *args para multiplicar. Crear una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variables como parámetros de la funcion y retornar como resultado la multiplicacion de todos los valores pasados como argumento.
import math
def multiplicar(*args):
    return math.prod(args)
print("El resultado de la multiplicacion es: ",multiplicar(2, 3, 4))
print("El resultado de la multiplicacion es: ",multiplicar(1, 5, 10, 2, 5))