# Ejercicio 5: Funciones - Convertidor de temperaturas
# Realizar dos funciones para convertir de grados Celsius 
# a Fahrenheit y viseversa.
# Fórmulas:
#   Celsius a Fahrenheit -> Grados Fahrenheit = (grados Celsius * 9/5) + 32
#   Fahrenheit a Celsius -> Grados Celsius = (grados Fahrenheit - 32) * 9/5

def menu():
    print('MENÚ')
    print('1. Celsius a Fahrenheit')
    print('2. Fahrenheit a Celsius')
    print('3. Salir')

def gradosC():
    gradosC = float(input('Ingrese los grados Celsius que desea pasar a Fahrenheit: '))
    gradosF = (gradosC * 9/5) + 32
    print(f'Los grados Celsius {gradosC} en grados Fahrenheit son: {gradosF} \n')

def gradosF():
    gradosF = float(input('Ingrese los grados Fahrenheit que desea pasar a Celsius: '))
    gradosC = (gradosF - 32) * 9/5
    print(f'Los grados Fahrenheit {gradosF} en grados Celsius son: {gradosC} \n')

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    print('')
    
    if opcion == '1':
        gradosC()
    elif opcion == '2':
        gradosF()
    elif opcion == '3':
        print("Saliendo del menú...")
        break


