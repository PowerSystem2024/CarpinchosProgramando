# Hacer un programa para calcular el factorial de un numero positivo

def factorial(n): # Creamos la funcion para calcular el factorial
    resultado = 1 # Iniciamos la variable en 1 ya que multiplicar por 1 no cambia el valor
    for i in range(1, n + 1): #  iteramos sobre todos los números desde 1 hasta n+1 (inclusive el ultimo numero).
        resultado *= i # En cada iteración del bucle, resultado se va a multiplicar por el valor actual de i
    return resultado

numero = int(input("Ingrese un numero para calcular su factorial: ")) # Se pide al usuario un numero

while numero < 0:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Introduce un número positivo: "))

if numero < 0: # Se evalua si el numero ingresado no es positivo
    print("El número debe ser positivo. Por favor, ingrese un número positivo.")
else:
    # Si es positivo, vamos a calcular el factorial
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")