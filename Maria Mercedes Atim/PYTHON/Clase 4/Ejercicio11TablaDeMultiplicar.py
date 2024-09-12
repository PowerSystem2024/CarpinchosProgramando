# Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10.
# Por ejemplo si ingresa 5, la lista tendra: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.

tablaDeMultiplicar = []

numero = int(input("Ingrese un numero para crear su tabla de multiplicar: "))

for i in range(1,11):
    tablaDeMultiplicar.append(numero*i)
    print(f"{numero} x {i} = {tablaDeMultiplicar[-1]}")
    
print(f"\nLa lista completa quedaria asi: {tablaDeMultiplicar}")