# Ejercicio 2:
# Determinar la solución lógica de la siguiente operación.
# ((3 + 5 x 8 ) < 3 and ((- 6/3 x 4 ) + 2 < 2)) or ( a > b)

print('((3 + 5 * 8 ) < 3 and ((- 6/3 * 4 ) + 2 < 2)) or ( a > b)')
a = int(input('Ingrese el valor de A: '))
b = int(input('Ingrese el valor de B: '))

resultado = ((3 + 5 * 8 ) < 3 and ((- 6/3 * 4 ) + 2 < 2)) or ( a > b)

print(f'((3 + 5 * 8 ) < 3 and ((- 6/3 * 4 ) + 2 < 2)) or ( {a} > {b})')
print(f'El resultado de la operación es: {resultado}')
