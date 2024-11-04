def sumar(a = 0, b = 0): #Le damos un valor por default.
    return a + b
resultado = sumar()
print(f"Resultado de la suma: {resultado}") # Muestra el valor por default
print(f"Resultado de la suma: {sumar(22,66)}") # Muestra el resultado