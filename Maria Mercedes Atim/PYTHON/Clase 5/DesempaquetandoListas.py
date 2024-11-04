# Desempaquetado de listas o list unpacking
def show(name, lastName): # Definimos la funcion para mostrar la lista
    print(name+" "+lastName) # La funcion imprimira nombre y apellido
person = ["Mercedes", "Atim"] # Creamos una lista
print("Pasamos uno por uno los datos de la lista a la función.")
show(person[0], person[1])
print("\nEsto es lo mismo que lo anterior pero le pasamos todo junto.")
show(*person) # Muestra todos los datos
print("\nDesempaquetamos la lista a traves de una tupla.")
persona2 = ("Paula", "Garin")
show(*persona2)
persona3 = {"lastName": "Rios", "name": "Nelson"} # Invertimos el ingreso de los datos con el diccionario
show(**persona3)