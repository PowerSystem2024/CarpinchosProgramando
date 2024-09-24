# Repaso del Ciclo for else
# Creación una lista de números 
numbers = [1, 2, 3, 4, 5]

# Creación de un ciclo for con una variable 'n'
for n in numbers:
    print(n)
    # Única forma de evitar que se ejecute el else
    # if n == 3:
    #     break
# El else se va a ejecutar siempre, incluso si la lista está vacía
else:
    print('Esto se terminó.')
