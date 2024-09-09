# Ejercicio:
# Calcular el factorial de un número mayor o igual a 0.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    print("El factorial de", numero, "es", factorial(numero))
