'''
# PRÁCTICA DE VARIABLES
# Variable tipo 'Entero'
miVariable = 3
print(miVariable)

# Variable tipo 'Caracter'
miVariable = "a"
print(miVariable)

# Variable tipo 'Real'
miVariable = 3.5
print(miVariable)

# Variable tipo 'Cadena'
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)

# Suma de variables
x = 10
y = 2
z = x + y

# Dirección de memoria de las literales
print(id(x))
print(id(y))
print(id(z))

# Clases de Datos
# Dato clase 'Entero (int)'
a = 10
print(type(a))
# Permite ver el clase de dato que se está almacenando.

# Dato clase 'Float (float)'
c = 10.78
print(type(c))

# Dato clase 'String (str) - Cadenas'
# Puede indicarse qué tipo es, una referencia.
b: str = "Hola mundo"
print(type(b))

# Manejo de Cadenas
# Concatenación de Cadenas
miGrupoFavorito = "G(i-dle):"
caracteristicas = "The best K-Pop group."
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

# Concatena, no suma
numero1 = "7"
numero2 = "8"
print(numero1+numero2)

# Al asignarle una clase 'Entero', los valores se suman
numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Dato clase 'Boolean (bool)'
# Permite definir si el valor es verdadero ('True') o falso ('False')
d = True
print(type(d))

miBooleano = 1 > 2
print(miBooleano)
if miBooleano:
    print("El resultado es verdadero.")
else:
    print("El resultado es falso.")

miBooleano2 = 3 > 2
print(miBooleano2)
if miBooleano2:
    print("El resultado es verdadero.")
else:
    print("El resultado es falso.")

# Procesar la entrada del usuario.
# Función Input
# resultado = input("Ingrese un número: ")  # Regresa un dato tipo string
# print(resultado)

# Conversión de la entrada de datos
numero1 = int(input("Escriba el primer número: "))
numero2 = int(input("Escriba el segundo número: "))
resultado = numero1 + numero2
print("El resultad de la suma es: ", resultado)

# OPERADORES ARITMÉTICOS
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("El resultado de la suma es: ", suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicación es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la división es: {division}')
division = operandoA // operandoB
print(f'El resultado de la división (int) es: {division}')
modulo = operandoA % operandoB
print(f'El resultado de la división o residuo (módulo) es: {modulo}')
exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')

# OPERADORES DE ASIGNACIÓN
miVariable3 = 10
print(miVariable3)

# Operadores de Reasignación
# Suma
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# Resta
miVariable3 -= 2
print(miVariable3)

# Multiplicación
miVariable3 *= 3
print(miVariable3)

# División
miVariable3 /= 2
print(miVariable3)

# OPERADORES DE COMPARACIÓN
# Igualdad
d = 4
b = 2
resultado = d == b
print(resultado)

#Diferencia
resultado = d != b
print(resultado)

# Mayor qué
resultado = d > b
print(resultado)

# Menor qué
resultado = d < b
print(resultado)

# Menor o Igual qué
resultado = d <= b
print(resultado)

# Mayor o Igual qué
resultado = d >= b
print(resultado)
'''
# OPERADORES LÓGICOS
a = False
b = False
resultado = a and b
print(resultado)

# Operador Or
resultado = a or b
print(resultado)

# Operador Not
resultado = not a
print(resultado)

