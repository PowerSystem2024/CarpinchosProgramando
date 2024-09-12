# Realiza un juego para adivinar el numero. Para ekki se debe generar un numero maleatorio entre 1 y 100 y luego ir pidiendo numeros indicando es mayor o menor, segun corresponda con respecto a n. El proceso termina cuando el usuario acierta y alli se debe mostrar el numero de intentos.

import random

aAdivinar = random.randint(1,100) # Guardamos un numero aleatorio
contador = 0

print("\n¡Bienvenido! Juguemos a adivinar el número.\n¿Podes adivinar el numero que estoy pensando de 1 a 100?\n")

while True:
    numero = int(input("Ingresa el numero: ")) # Pedimos al usuario un numero
    contador += 1 # Aqui guardamos el numero de intentos
    if aAdivinar < numero: # Si el numero a adivinar es menor
        print("\t¡uy, intenta de nuevo! El numero es menor")
    elif numero < aAdivinar: # Si el numero a adivinar es mayor
        print("\t¡uy, intenta de nuevo! El numero es mayor")
    else:
        print(f"¡Genial, adivinaste! El numero es {aAdivinar}, intentaste {contador} veces.")
        break