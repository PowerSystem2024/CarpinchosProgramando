# Hacer un programa que pida una cadena por teclado, luego guardar los caracteres en una lista sin repetir caracteres.
frase = input("Ingrese una frase: ")

sinRepetir = set(frase)  # Convertir la cadena a conjunto

listaSinRepetir = list(sinRepetir)  # Convertir el conjunto a lista

print("La frase sin caracteres repetidos queda asi: ", listaSinRepetir)
