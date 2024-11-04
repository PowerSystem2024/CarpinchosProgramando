# Raiz cuadrada de un numero positivo.
# Importamos la clase Math para hacer uso de la funcion sqrt() square root (Raiz cuadrada)
import math

# Solicitamos al usuario que ingrese un número positivo
numero = int(input("Ingrese un numero positivo: "))

# Mientras el número ingresado sea negativo, seguimos solicitando un número positivo
while numero < 0:
    print("Error, el número debe ser positivo")
    numero = int(input("Ingrese un número positivo: "))

# Calculamos y mostramos la raíz cuadrada del número ingresado
print(f"La raíz cuadrada de {numero} es: {math.sqrt(numero):.2f}")
