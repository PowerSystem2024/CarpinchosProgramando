# NÚMEROS PARES O IMPARES
# 1. Solicitar que el usuario ingrese un número.
# 2. Este número se asigna a una variable.
# 3. Utilizar la estructura 'if else'.
# 4. La fórmula: <num>%2==0 indica si el número es par.
# 5. Si es TRUE: imprimir que es par.
# 6. Si es FALSE: imprimir que es impar.

numero = int(input("Escriba un número:"))
print(f'El resultado de la división del número elegido es: {numero % 2}.')

if numero % 2 == 0:
    print(f'El numero {numero} es PAR.')
else:
    print(f'El número {numero} es IMPAR.')
