# Ejercicio: Tipos de Números
# Leer 10 números e imprimir cuántos son positivos, cuántos negativos y cuántos neutros.

positivos = 0
negativos = 0
neutros = 0

for _ in range(10):
    num = float(input('Ingrese un número: '))

    if num > 0:
        positivos += 1
    elif num == 0:
        neutros += 1
    else:
        negativos += 1

print(f'Cantidad de números positivos: {positivos}')
print(f'Cantidad de números negativos: {negativos}')
print(f'Cantidad de números neutros: {neutros}')
