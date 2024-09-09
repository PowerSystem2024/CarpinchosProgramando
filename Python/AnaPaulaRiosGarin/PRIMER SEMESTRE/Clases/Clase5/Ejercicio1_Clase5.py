# Ejercicio 1: Mayor de 2 números.
# Solicitar al usuario dos valores, determinar cuál es el mayor.
# 1. Solicitar al usuario dos valores: 
#   numero1 (int)
#   numero2 (int)
# 2. Se debe imprimir el mayor de los dos números (La salida debe ser idéntica a la siguiente):
#   Ingrese el valor para el número 1:
#   Ingrese el valor para el número 2:
#   El número mayor es: <numeroMayor>

numero1 = int(input("Ingrese el valor para el número 1:"))
numero2 = int(input("Ingrese el valor para el número 2:"))

if numero1 > numero2:
    print('El número 1 es mayor')
else:
    print('El número 2 es mayor')
