# Ejercicio 1:
# Escribir la siguiente expresión en forma de expresión algorítmica:
#      a3 x (b2 – 2ac)
#            2b
# 1. Pedirle al usuario 3 valores = a, b, c.
# 2. Mostrar el resultado final.

print('''
    Dada la siguiente operación:
      ax3 x (bx2 – 2xaxc)
            2xb      
''')

a = float(input('Ingresar el valor de A: '))
b = float(input('Ingresar el valor de B: '))
c = float(input('Ingresar el valor de C: '))

resultado = (a*3 * (b*2 -2*a*c))/2*b

print(f'''
      {a}x3 x ({b}x2 – 2x{a}x{c})
            2x{b}      
''')

print(f'El resultado de la operación es: {resultado}')
