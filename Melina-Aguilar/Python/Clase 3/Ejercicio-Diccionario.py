# Ejercicio: La tarea consiste en ingresar elementos al diccionario llamado seleccionArgentina, 
#           los elementos a ingresar deben ser como mínimo 4, estos elementos son los jugadores
#           con su número de camiseta, nombre, apellido, edad, altura, precio y posición de juego.

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': ' Extremo derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millonres', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Poscion': 'Portero'},
    9: {'Nombre': 'Julian Alvarez', 'Edad': 24, 'Altura': 1.7, 'Precio': '90 millones', 'Posicion': 'Delantero central'},
    24: {'Nombre': 'Enzo Fernandez', 'Edad': 23, 'Altura': 1.78, 'Precio': '75 millones', 'Posicion': 'Mediocampista'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 30, 'Altura': 1.82, 'Precio': '8 millones', 'Posicion': 'Centrocampista'},
    25: {'Nombre': 'Lisandro Martinez', 'Edad': 26, 'Altura': 1.75, 'Precio': '50 millones', 'Posicion': 'Defensa Central'},
    22: {'Nombre': 'Lautaro Martinez', 'Edad': 27, 'Altura': 1.74, 'Precio': '110 millones', 'Posicion': 'Defensa Central'},
}

print(seleccionArgentina)
print(seleccionArgentina[10])

# Recorremos las llaves del diccionario | con 'for' in seleccionArgentina solo me muestra las llaves
for llave in seleccionArgentina:
    print(llave)
    
# Recorremos los valores del diccionario | .values()
for valor in seleccionArgentina.values():
    print(valor)
    
# Recorremos todos los datos | .items()
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Cantidad de jugadores cargados en el diccionario:',end=' ')
print(len(seleccionArgentina))  # Vemos la cantidad de elementos que tiene el diccionario