# Funciones: Palabra return
# Creación de una función para sumar
def sumar(a, b):
    # Hay dos opciones
    # 1. Asignar a una variable el resultado de la operación y esa es la variable que se va a retornar
    # 2. Regresar el resultado de la operación con la palabra 'return' 
    # haciendo la operación dentro del bloque
    return a + b 

# Creación de una variable y llamado a la función
# Aquí la función necesita que se le introduzcan los argumentos
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')
