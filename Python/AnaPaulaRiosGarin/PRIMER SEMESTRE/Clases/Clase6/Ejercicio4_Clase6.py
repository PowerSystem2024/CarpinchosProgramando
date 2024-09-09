# Ejercicio 4: Área y longitud de un círculo
# Hacer un programa para ingresar el radio de un círculo y se reporte su área y la longitud de la circunferencia.
# Área = Pi * r2
# Longitud = 2 * Pi * r
# En este ejercicio vamos a necesitar importar el módulo math porque tiene el valor de Pi.
# Se escribe: import math.

import math

radio = float(input("Ingrese el radio del círculo: "))

area = math.pi * radio ** 2

longitud = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")
