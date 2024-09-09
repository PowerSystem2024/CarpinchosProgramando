# Ejercicio: Rango entre las edades 20 y 30 años.
# 1. Preguntarle la edad al usuario.
# 2. Si la edad está dentro de los 20 o 30 años, está dentro del rango.
# 3. Combinar los operadores 'and' y 'or' para saber si el usuario está dentro del rango o no.

edad = int(input('Ingrese su edad:'))

veinte = edad >= 20 and edad < 30
print(veinte)

treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    print(f'La edad de {edad} años está dentro del rango de edad.')
else:
    print(f'la edad de {edad} años no está dentro del rango de edad.')
