seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 37, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Delantero"},
    11: {"Nombre": "Angel Di Maria", "Edad": 36, "Altura": 1.78, "Precio": "3 Millones", "Posicion": "Extremo derecho"},
    21: {"Nombre": "Paulo Dybala", "Edad": 30, "Altura": 1.77, "Precio": "20 Millones", "Posicion": "Mediapunta"},
    30: {"Nombre": "Nicolas Otamendi", "Edad": 36, "Altura": 1.83, "Precio": "1 Millon", "Posicion": "Defensa central"},
    1: {"Nombre": "Franco Armani", "Edad": 37, "Altura": 1.89, "Precio": "1 Millon", "Posicion": "Portero"},
    8: {"Nombre": "Enzo Fernandez", "Edad": 23, "Altura": 1.78, "Precio": "75 Millones", "Posicion": "Mediocentro"},
    19: {"Nombre": "Julian Alvarez", "Edad": 24, "Altura": 1.70, "Precio": "90 Millones", "Posicion": "Delantero centro"},
    17: {"Nombre": "Cristian Romero", "Edad": 26, "Altura": 1.85, "Precio": "65 Millones", "Posicion": "Defensa central"},
    15: {"Nombre": "Gonzalo Montiel", "Edad": 27, "Altura": 1.75, "Precio": "10 Millones", "Posicion": "Lateral derecho"}
}

print(seleccionArgentina) # Muestra todo el diccionario
print("\n",seleccionArgentina[19]) # Muestra un elemento del diccionario, se invoca con clave.
print("\n---- Valores del diccionario: ---- ",seleccionArgentina.values()) # Muestra los valores del diccionario, se incova con values() -> valor.

print("\n---- Recorremos el diccionario con FOR para obtener la clave: ----")
for llave in seleccionArgentina:
    print(llave)

print("\n---- Recorremos el diccionario con FOR para obtener el valor: ----")
for valor in seleccionArgentina.values():
    print(valor)

print("\n---- Recorremos el diccionario con FOR para obtener clave y valor: ----")
for clave, valor in seleccionArgentina.items():
    print(clave, valor)

print("\nTenemos cargados en el diccionario la cantidad de:", end=" ")
print(len(seleccionArgentina),"jugadores de la seleccion Argentina.")

for i in seleccionArgentina:
    print(f"\n{i} -> {seleccionArgentina[i]}")