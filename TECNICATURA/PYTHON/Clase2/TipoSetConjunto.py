# Los sets no tienen indice, por lo mismo no son ordenados. Pero nos sirve para listas donde se repiten los elementos ya que muestra solo 1 si estan repetidos.

print("Creamos un set llamado Planeta, que contiene los siguientes elementos: ")
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

print("\nVer la cantidad de elementos en el set: ")
print(len(planetas)) # Vemos la dimension del set. La cantidad de elementos.

# Ver si un elemento existe dentro de set.
print("\nVer si un elemento existe dentro de set: ")
print("Mercurio" not in planetas) #Ser cuidadosos y respetar mayusculas o minusculas para que coincida.

print("\nAgregamos un nuevo elemento al set: ")
planetas.add("Tierra") #con add agregamos elementos, no se agregan duplicados. Solamente una vez se muestran.
print(planetas)

print("\nEliminamos un elemento del set: ") #Nos puede dar error si el elemento no existe.
planetas.remove("Jupiter")
print(planetas)
planetas.discard("Tierra") #Discard es descartar,a diferencia de remove, no rompe la ejecucion si ingresamos mal el elemento.

print("\nPodemos organizar elementos del set: ") #Nos puede dar error si el elemento no existe.
planetasOrdenados = sorted(planetas)
print(planetasOrdenados)

print("\nPara eliminar los elementos del set: ") #Nos puede dar error si el elemento no existe.
planetas.clear()
print(planetas) # muestra el conjunto vacío.

print("\nUsamos DEL para eliminar el set: ") #Nos puede dar error si el elemento no existe.
del planetas
print(planetas) # Nos va a mostrar error ya que eliminó el conjunto.