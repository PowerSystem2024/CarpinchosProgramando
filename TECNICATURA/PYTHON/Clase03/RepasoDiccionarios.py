diccionarioNuevo = {"Azul": "Blue", "Rojo": "Red", "Verde": "Green", "Amarillo": "Yellow"}
print(diccionarioNuevo)

print("\nEliminamos elementos del diccionario: ")
del(diccionarioNuevo["Azul"])
print(diccionarioNuevo)

print("\nLos diccionarios pueden almacenar diferentes tipos de dato: ")
diccionario2 = {"Mercedes": {"Edad": 36, "Altura": 1.54}, "Leonel": [32, 1.75], "Raul": [35, 1.78]}
print(diccionario2)