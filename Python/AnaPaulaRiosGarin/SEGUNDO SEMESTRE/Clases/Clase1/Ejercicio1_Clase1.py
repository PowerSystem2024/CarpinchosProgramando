# Ejercicio 1: Uso de Rangos 
# Iterar un rango de 0 a 10 e imprimir los números divisibles por 3.
# Es decir, imprimir 0, 3, 6, 9.

rango = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Rango de 0 a 10.')
print(rango)

print('Los números divisibles por 3 son:')
for i in range(11):
    if i%3 == 0:
        print(i)

