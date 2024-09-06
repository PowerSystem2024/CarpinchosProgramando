print("---- VERIFICAR SUBCONJUNTOS: ----")
conjunto1 = {"bye", "Hola"}
conjunto2 = {7,"hola"}
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Devuelve un booleano
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print("\n---- VERIFICAR SUPERCONJUNTOS: ----")
# Verifica si conjunto3 es superconjunto de 1, es decir si los elementos del conjunto1 esran en el conjunto3
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2)) # devuelve un booleano
print(conjunto1.issuperset(conjunto3))
print(conjunto2.issuperset(conjunto3))

print("\n---- VERIFICAR CONJUNTOS DISCONEXOS: ----")
# Conjuntos que no comparten ningun elemento en comun.
print(conjunto1.isdisjoint(conjunto2))

print("\n---- CONVERTIR CONJUNTO EN INMUTABLE: ----")
# Esto hace que el conjunto no se pueda modificar, eliminar o agregar elementos
conjunto1 = frozenset