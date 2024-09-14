# Escriba un programa donde cree una lista con los personajes del señor de los anillos.

personajes = [] #Creamos la lista donde vamos a guardar los diccionarios de los personajes.

P1 = {"Nombre": "Aragorn", "Clase": "Guerrero", "Raza": "Dunadan del Norte"} # creamos el primer diccionario
personajes.append(P1) # Agregamos a la lista vacía
P2 = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istari"}
personajes.append(P2)
P3 = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(P3)
P4 = {"Nombre": "Thranduil", "Clase": "Rey", "Raza": "Elfo Sindar"}
personajes.append(P4)
P5 = {"Nombre": "Eomer", "Clase": "Guerrero", "Raza": "Dunadan de Rohan"}
personajes.append(P5)
P6 = {"Nombre": "Eowyn", "Clase": "Guerrera", "Raza": "Dunadan de Rohan"}
personajes.append(P6)

print(f"La lista con los personajes quedaria asi: {personajes}")