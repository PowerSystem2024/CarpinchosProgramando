# REPASO DICCIONARIO
# del (diccionarioNuevo["Azul"])
# print(diccionarioNuevo)

# Diccionarios con diferentes tipos de datos
diccionario2 = {
    "Mercedes": {"Edad": 40, "Altura": 1.83},
    "Miguel": [45, 1.85],
    "Wanda": [35, 1.67]
}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 millones", "Posición": "Extremo derecho"},
    11: {"Nombre": "Ángel Di María", "Edad": 34, "Altura": 1.80, "Precio": "12 millones", "Posición": "Extremo derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 millones", "Posición": "Media Punta"},
    19: {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "50 millones", "Posición": "Defensa central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 millones", "Posición": "Arquero"},
    7: {"Nombre": "Rodrigo De Paul", "Edad": 28, "Altura": 1.80, "Precio": "40 millones", "Posición": "Mediocampista"},
    3: {"Nombre": "Nicolás Tagliafico", "Edad": 30, "Altura": 1.72, "Precio": "9 millones", "Posición": "Lateral izquierdo"},
    22: {"Nombre": "Lautaro Martínez", "Edad": 25, "Altura": 1.74, "Precio": "75 millones", "Posición": "Delantero centro"},
    8: {"Nombre": "Marcos Acuña", "Edad": 31, "Altura": 1.72, "Precio": "12 millones", "Posición": "Lateral izquierdo"}
}

#for llave, valor in seleccionArgentina.items()
#    print(llave, valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end)
print(len(seleccionArgentina))

#Pilas usando listas 
pila = [1, 2, 3]

#agregar elementos a la pila por el final 
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #quita el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elemento{elementoBorrado}")
print(f"La fila ahora quedo asi ")

#Colas con listas 
#Estructuras de datos tipo fifo( first input /first output)

cola = ["Ariel", "Nicolas", "Fernando", "Mercedes"]
cola.append("Wanda")
cola.append("Miguel")
print (cola)

#Sacamos elementos de la cola 
seRetira = cola.pop(0)
print(f"Atendido{seRetira}")
print (cola)
