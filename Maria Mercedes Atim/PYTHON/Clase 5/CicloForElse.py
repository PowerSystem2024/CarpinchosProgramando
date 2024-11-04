numbers = [1, 2, 3, 4, 5]
for numero in numbers:
    print(numero)
    if numero == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termina")