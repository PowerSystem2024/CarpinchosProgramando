# Escriba un programa donde cree una lista y que a continuación
# elimine los elementos repetidos. Por último mostrar la lista.

conRepetidos = [1, 1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 9, 9, 9, 9] # Lista con elementos repetidos.

sinRepetidos = list(set(conRepetidos)) # Convertimos la lista a conjunto para eliminar los repetidos.

print(f"La lista con datos repetidos se ve asi: {conRepetidos}")
print(f"Asi queda la lista con elementos sin repetir: {sinRepetidos}")