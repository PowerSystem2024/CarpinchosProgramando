# Sintaxis de range(inicio<opcional>, fin <requerido>, incremento <opcional>)


# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles en 3
# Ejemplo de ejecucion: 0, 3, 6, 9

print('Rango de 0 a 10 con numeros divisibles entre 3')

for numero in range(0, 11):  # range(0, 11) genera números desde 0 hasta 10 (11 no está incluido)
    if numero % 3 == 0:  # Verifica si el número es divisible por 3
        print(numero)  # Imprime el número si es divisible por 3