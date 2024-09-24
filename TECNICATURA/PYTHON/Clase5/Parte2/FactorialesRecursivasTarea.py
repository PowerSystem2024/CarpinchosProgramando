# Funciones recursivas con factorial - TAREA
def num(numero):
    if numero == 1:
        return 1
    else:
        return numero * num(numero - 1)

numFactorial = input(int('Ingrese el número del que desea obtener la factorial: '))
resultado = num(numFactorial)
print(f'El factorial del número {numFactorial} es: {resultado}')
