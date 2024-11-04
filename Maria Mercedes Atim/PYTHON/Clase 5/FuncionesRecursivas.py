# Funciones recursivas
def factorial(numero):
    if numero == 1: # caso base
        return 1
    else:
        return numero * factorial(numero-1) # caso recursivo
resultado = (factorial(5))
print("\nEl factorial del numero 5 es: ", resultado)

print("\n--- Tarea: Solicitar al usuario el numero para calcular el factorial ---")

numero = int(input("\nIngrese un numero: "))
print(f"El resultado del factorial de {numero} es:  {factorial(numero)}")