# Ejercicio 2: Agenda Telefónica
# Hacer un programa que simule una agenda de contactos. Crear un diccionario en donde la clave sea el nombre del usuario y el valor sea el teléfono, el programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

agenda = {
    'Ana': {'Número': '11 3456-2314'},
    'Nelson': {'Número': '11 2357-7895'},
    'Mercedes': {'Número': '11 0951-2345'},
    'Mariana': {'Número': '11 2140-2421'},
    'Wanda': {'Número': '11 3242-7864'},
    'Nicolás': {'Número': '11 7640-5620'},
    'Melina': {'Número': '11 5547-9986'},
    'Cirano': {'Número': '11 3258-0970'},
}

def menu():
    print('AGENDA DE CONTACTOS')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')

def contactoNuevo():
    nombre = input("Ingrese el nombre del nuevo contacto: ")
    if nombre in agenda:
        print(f"El contacto {nombre} ya existe. \n")
    else:
        numero = input(f"Ingrese el número de {nombre}: ")
        agenda[nombre] = {'Número': numero}
        print(f"Contacto {nombre} agregado correctamente. \n")

def borrarContacto():
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} borrado correctamente. \n")
    else:
        print(f"El contacto {nombre} no existe. \n")

def verAgenda():
    if agenda:
        print("AGENDA DE CONTACTOS")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {info['Número']}")
        print('')
    else:
        print("No hay contactos en la agenda. \n")

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    print('')
    
    if opcion == '1':
        contactoNuevo()
    elif opcion == '2':
        borrarContacto()
    elif opcion == '3':
        verAgenda()
    elif opcion == '4':
        print("Saliendo de la agenda...")
        break
    else:
        print("La opción seleccionada no está disponible, intente de nuevo. \n")
