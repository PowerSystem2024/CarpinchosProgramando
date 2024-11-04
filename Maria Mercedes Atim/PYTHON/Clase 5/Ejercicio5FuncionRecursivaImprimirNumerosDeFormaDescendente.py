# Imprimir numeros de 5 a 1 de manera descebdebte usando funciones recursivas. Puede ser cualquier valor positivo. Si se ingresan negativos no imprimir nada.

def imprimirDescendente(numero):
    if numero <= 0: # Nos aseguramos de que imprima si el nro es positivo
        return
    print(numero) # Imprime el número actual
    imprimirDescendente(numero - 1) # resta un numero al actual

print("\nNumeros descendentes desde 5:")
imprimirDescendente(5)
print("\nNumeros descendentes desde 3:")
imprimirDescendente(3)

imprimirDescendente(-7) # No imprime nada