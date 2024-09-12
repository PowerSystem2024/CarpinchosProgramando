# Escriba un programa que tenga 2 listas. Y que a continuacion cree listas:
# (No deben contener repetidos).
# • Lista de palabras que aparecen en las listas.
# • Lista de palabras que aparecen en la primera lista pero no en la segunda.
# • Lista de palabras que aparezcan en la segunda lista pero no en la primera.
# • Lista de palabras que aparezcan en ambas listas.

primeraLista = ["Rottweiller", "Caniche", "Mestizo", "Mestizo", "Dogo", "Labrador", "Dogo"]
segundaLista = ["Caniche", "Bulldog", "Bulldog", "Beagle", "Rottweiller", "Husky", "Dogo"]

primeraListaSinRepetidos = set(primeraLista) # Eliminamos los repetidos de la lista
segundaListaSinRepetidos = set(segundaLista) # Eliminamos los repetidos de la lista

# • Lista de palabras que aparecen en las listas.
unionConjuntos = primeraListaSinRepetidos.union(segundaListaSinRepetidos) # se unen los conjuntos
listaUnion = list(unionConjuntos) # convertimos a lista el conjunto
print(f"Lista de palabras que aparecen en las listas: {listaUnion}")

# • Lista de palabras que aparecen en la primera lista pero no en la segunda.
elementosPrimeraLista = primeraListaSinRepetidos.difference(segundaListaSinRepetidos) # diferencia entre el 1ro y el 2do
listaElementosPrimeraLista = list(elementosPrimeraLista) # conversion a lista
print(f"Lista de palabras que aparecen en la primera lista pero no en la segunda: {listaElementosPrimeraLista}")

# • Lista de palabras que aparezcan en la segunda lista pero no en la primera.
elementosSegundaLista = segundaListaSinRepetidos.difference(primeraListaSinRepetidos) # diferecia entre el 2do con el 1ro
listaElementosSegundaLista = list(elementosSegundaLista) # conversion a lista
print(f"Lista de palabras que aparecen en la segunda lista pero no en la primera: {listaElementosSegundaLista}")

# • Lista de palabras que aparezcan en ambas listas.
elementosEnAmbas = primeraListaSinRepetidos.intersection(segundaListaSinRepetidos)
listaElementosEnAmbas = list(elementosEnAmbas)
print(f"Lista de palabras que aparezcan en ambas listas: {listaElementosEnAmbas}")