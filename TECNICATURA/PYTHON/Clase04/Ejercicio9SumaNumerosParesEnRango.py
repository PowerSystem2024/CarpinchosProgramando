# Hacer un programa para sumar numeros pares dentro de un rango. Por ejemplo:
# Suma de numeros pares del 2 al 30
# Suma = 240
suma = 0 # Inicializamos suma en cero, para poder usarla despues
rango = range(0,50) # establecemos un rango de 0 a 50

for numero in rango:
    if (numero % 2 == 0): # Tomamos los numeros pares y los sumamos
        suma += numero # Guardamos la suma en la variable suma que definimos al principio
        
print(f"La suma de los numeros pares dentro del rango es: {suma}")