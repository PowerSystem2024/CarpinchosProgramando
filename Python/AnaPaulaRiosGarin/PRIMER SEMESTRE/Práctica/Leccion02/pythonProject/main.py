'''
# Sentencia if/else
condicion = True
if condicion == True:
    print('Condición verdadera.')
elif condicion == False:
    print('Condición falsa.')
else:
    print('Condición sin especificar.')

# Conversión de Número a Texto
num = int(input('Ingrese un número en el rango del 1 al 3: '))
numTexto = ''
if num == 1:
    numTexto = 'Número UNO.'
elif num == 2:
    numTexto = 'Número DOS.'
elif num == 3:
    numTexto = 'Número TRES.'
else:
    numTexto = 'El número ingresado está fuera del rango.'
print(f'El número ingresado es: {num} - {numTexto}')
'''
condicion = True 
# if condicion:
#    print('Condición verdadera.')
# else:
#    print('Condición falsa.')
print('Condición verdadera') if condicion else print('Condición falsa.')
