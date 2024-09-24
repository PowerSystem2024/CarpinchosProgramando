# Funciones recursivas con factorial
def factorial(numero):
    # Caso Base
    if numero == 1:
        return 1
    else:
        # Caso Recursivo
        return numero * factorial(numero - 1)

# Resultado en código duro
resultado = factorial(5)
print(f'El factorial del número 5 es: {resultado}')
