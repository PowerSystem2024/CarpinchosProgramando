# Ejercicio 1: Calcular la Estación del Año
# Pedirle al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12, luego hay que indicarle en qué estación del año está:
#     VERANO             OTOÑO           INVIERNO        PRIMAVERA
# 21/12 al 21/03    21/03 al 21/06  21/06 al 21/09    21/09 al 21/12
#   1, 2, 3            4, 5, 6          7, 8, 9         10, 11, 12
# En el ejercicio utilizar 'None': Esto indica que la variable aún no tiene asignado un valor (está vacía), luego se ampliará. Este 'None' es equivalente a 'null' en otros lenguajes de programación (como Java).

mes = None
mes = int(input('Ingrese un número de un mes del año (1-12): '))

if mes[1, 2, 3]:
    print('La estación del mes número {mes} es VERANO.')
elif mes[4, 5, 6]:
    print('La estación del mes número {mes} es OTOÑO.')
elif mes[7, 8, 9]:
    print('La estación del mes número {mes} es INVIERNO.')
elif mes[10, 11, 12]:
    print('La estación del mes número {mes} es PRIMAVERA.')
else:
    print('Número de mes inexistente, ingrese un número de un mes del año (1-12).')
