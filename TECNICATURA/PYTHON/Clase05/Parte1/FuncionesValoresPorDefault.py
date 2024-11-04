# Funciones: Valores por Default en Argumentos
# Creación de función
# Declarar que los argumentos son de tipo entero no determinará el tipo de valor que tendrán
def sumar(a:int = 0, b:int = 0) -> int:
    return a + b

# resultado tirará error porque faltan los argumentos requeridos, 
# para evitar esto es necesario ponerle un valor por default a los mismos
resultado = sumar()

# Imprime el resultado default
print(f'Resultado de la suma: {resultado}')

#Imprime el resultado con los valores pasados en el print
print(f'Resultado de la suma: {sumar(22, 66)}')
