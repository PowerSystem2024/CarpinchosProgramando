# Ejercicio Grupal
# Calcular la suma de 'n' primeros números.

n = int(input('Ingrese la cantidad de números a sumarse: '))

suma = 0
contador = 0

while contador <= n:
    print('Sumando los números...', contador)
    suma += contador
    contador += 1
else:
    print('Fin de la suma.')

print('La suma de los primeros', n, 'números es:', suma)
