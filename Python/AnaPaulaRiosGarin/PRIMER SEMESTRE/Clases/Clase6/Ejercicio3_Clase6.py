# Ejercicio 3: 
# Intercambiar el valor de dos variables.
# Por ejemplo: 
#   a = 10 -> a = 5
#   b = 5 -> b = 10

a = 10
b = 5
print('VALORES ORIGINALES')
print('a =', a)
print('b =', b)

a, b = b, a
print('VALORES INTERCAMBIADOS')
print('a =', a)
print('b =', b)
