# List comprehension, lista de comprensión
# No modifica la lista original, solo extrae los elementos especificados.
nombres = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
nombresConP = [elemento for elemento in nombres if elemento[0] == "p"] # esto regresa una nueva lista
print(nombresConP)

# Diccionario
cervezas = [{"name": "Quilmes", "country": "Arg"},
                    {"name": "Corona", "country": "Mex"},
                    {"name": "Stella Artois", "country": "Belgium"}
                    ]
Arg = [elemento for elemento in cervezas if elemento["country"] == "Arg"]
print(" --- Diccionario completo: ",cervezas,"\n --- Diccionario con elemento especificado: ",Arg)