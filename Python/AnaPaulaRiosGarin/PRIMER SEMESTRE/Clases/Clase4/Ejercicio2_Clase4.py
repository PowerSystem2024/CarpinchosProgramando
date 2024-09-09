# DETERMINAR SI ES MAYOR DE EDAD
# 1. Pedir un número al usuario.
# 2. Almacenar el valor en una variable.
# 3. Usar la estructura 'if else'
# 4. La fórmula es: <num> >= 18.
# TRUE: Imprimir que la persona es mayor de edad.
# FALSE: Imprimir que la persona es menor de edad.

edad = int(input("Ingrese su edad:"))

if edad >= 18:
    print("Usted es MAYOR de edad.")
else:
    print("Usted es MENOR de edad.")
