# Menu interactivo - Cajero Automatico
# Hacer un programa que simule un cajero automatico con un saldo inicial de $1000 tendra el siguiente menu de opciones:
# • Ingresar dinero a la cuenta.
# • Retirar dinero de la cuenta
# • Mostrar dinero disponible
# • Salir

saldo = 1000 # Iniciamos saldo con 1000 pesos

while True:
    print("\t--- MENU ---")
    print("1. Ingresar dinero a la cuenta.")
    print("2. Retirar dinero de la cuenta.")
    print("3. Mostrar dinero disponible.")
    print("4. Salir.")
    
    opcion = int(input("\nIngrese una opcion del menu: ")) # Solicitamos al usuario que ingrese una opcion

    if opcion == 1:
        ingresar = float(input("\n¿Cuanto dinero desea ingresar? $ "))
        saldo += ingresar # Se suma lo que ingrese el usuario
        print(f" \nSaldo actualizado: Hay ${saldo}.\n")
    elif opcion == 2:
        retirar = float(input("\n¿Cuanto dinero desea retirar? $ "))
        if retirar > saldo: # Si el usuario quiere retirar mas de lo que tiene en la cuenta
            print(f"\nSu saldo es insuficiente para retirar esa cantidad. Actualmente tiene: ${saldo}\n")
        else:
            saldo -= retirar # Si tiene saldo suficiente para retirar, se resta lo que retira del saldo.
            print(f"\nSaldo actualizado: Su saldo es ${saldo}.\n") # Se muestra el saldo
    elif opcion == 3:
        print(f"\nSu saldo es ${saldo}.\n")
    elif opcion == 4:
        print("-----------------------------------------------------")
        print("Gracias por usar el cajero automático. ¡Hasta pronto!")
        print("-----------------------------------------------------")
        break
    else:
        print("Opcion incorrecta.\n")