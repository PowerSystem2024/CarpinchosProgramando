# Colas con listas
# Estructura de datos de tipo fifo(first input / first output (primero en entrar / primero en salir))

cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregando elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')

print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)  # Se retira la posicion 0

print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)      # Aqui continua con el siguiente

print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)  # Se retira la posicion 0

print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)  # Se retira la posicion 0

print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)  # Se retira la posicion 0

print(f'Atendido el cliente {seRetira}')
print(cola)