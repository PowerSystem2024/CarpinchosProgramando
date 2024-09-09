# Ejercicio: Año Bisiesto
# Diseñar un programa que ingresado un año, devuelva por consola si es un año bisiesto o no, repetir la acción hasta que el usuario lo decida. 

def esBisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


while True:
    anio = int(input("Ingresa un año para verificar si es bisiesto: "))
    if esBisiesto(anio):
        print(anio, "es un año bisiesto.")
    else:
        print(anio, "no es un año bisiesto.")

    opcion = input("¿Deseas verificar otro año? (1: Sí, 0: No): ")
    if opcion != "1":
        break
