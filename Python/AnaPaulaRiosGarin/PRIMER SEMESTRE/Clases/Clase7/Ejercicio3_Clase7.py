# Ejercicio 3: Sistema de Calificaciones
# El objetivo del programa será crear un sistema de calificaciones de la siguiente manera:
# Pedirle al usuario que ingrese un valor del 0 al 10.
# Luego, si se ingresa 9 o 10, imprimir A
# Luego, si se ingresa 8 y menor a 9, imprimir B
# Luego, si se ingresa 7 y menor a 8, imprimir C
# Luego, si se ingresa 6 y menor a 7, imprimir D
# Luego, si se ingresa 0 y menor a 6, imprimir F
# De lo contrario, imprimir 'El valor ingresado es incorrecto.'.

calificacion = float(input('Ingrese su calificación (1-10): '))
letraCalificacion = None

if 9 <= calificacion <= 10:
    letraCalificacion = "A"
elif 8 <= calificacion <= 9:
    letraCalificacion = "B"
elif 7 <= calificacion <= 8:
    letraCalificacion = "C"
elif 6 <= calificacion <= 7:
    letraCalificacion = "D"
elif 0 <= calificacion <= 6:
    letraCalificacion = "F"
else:
    print('Valor ingresado incorrecto.')

if letraCalificacion is not None:
    print(f'Su calificación es: {letraCalificacion}')
    