# Hacer un programa que simule una agenda de contactos. Crear un diccionario
# donde la clave sea el nombre del usuario y el valor sea el telefono. El programa
# tendrá el siguiente menú de opciones:
# 1. Nuevo contacto.
# 2. Borrar contacto.
# 3. Ver contacto existente.
# 4. Salir.

agenda = {}

while True:
    print("\n -- MENU --")
    print("1. Nuevo contacto.")
    print("2. Borrar contacto.")
    print("3. Ver contacto existente.")
    print("4. Salir.")
    
    opcion = int(input("\nIngrese una opción del menú: ")) # Solicitamos al usuario una opcion del menu
    
    if opcion == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("\nContacto agregado exitosamente.")
        else:
            print("Este contacto ya existe.")
    
    elif opcion == 2:
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        if nombre in agenda:
            del agenda[nombre]
            print("\nSe eliminó el contacto especificado.")
        else:
            print("Este contacto no existe en la agenda.")
    
    elif opcion == 3:
        print("\n----------------------")
        print("Agenda de contactos: ")
        print("----------------------\n")
        if not agenda:
            print("La agenda está vacía.")
        else:
            for clave, valor in agenda.items():
                print(f"Nombre: {clave}, Teléfono: {valor}")
    
    elif opcion == 4:
        print("\n - ¡Gracias por utilizar su agenda de contactos! - ")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
