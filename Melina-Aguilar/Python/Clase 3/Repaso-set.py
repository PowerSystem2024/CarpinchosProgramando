# REPASO DE SET O CONJUNTO {}

# Son grupos de elementos desordenados. Su principal caracteristica es que no pueden
# haber duplicados. 
# Dentro de un conjunto hay valores UNICOS y puede tener diferentes tipos de datos.


# # Para definir un conjunto
conjunto2 = set()
conjunto1 = { 'bye',}            # con {} no puede estar vacio, solo 'set()'. Aqui ya debe haber algo que lo identifique como conjunto, si no, no podemos agregar nada. 

conjunto1.add('hola')
conjunto2.add(7)                 # Con '.add' podemos ir ingresando de a UN elemento
conjunto2.add('Hola')            
print(conjunto2)

conjunto1.add(9)              
print(conjunto1)

# No se pueden agregar varios elementos al mismo tiempo en un conjunto
# conjunto1.add(7, 8, 9)  #sale error


print(3 not in conjunto1)   # Preguntamos si el '3' NO esta en 'conjunto1'


# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)  # Nos devuelve un booleano



# --- Operaciones en conjuntos---

# Union de conjuntos
conjunto3 = conjunto1 | conjunto2       # La linea une ambos conjuntos
print(conjunto3)

# Interseccion de conjuntos (el elemento que tienen en comun)
conjunto3 = conjunto1 & conjunto2
print(conjunto3)

# Mostramos que elementos hay en el conjunto 1 y no el 2
conjunto3 = conjunto1 - conjunto2
print(conjunto3)

# Mostramos que elementos hay en el conjunto 2 y no el 1
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

# Diferencia simetrica  (Muestra elementos que estan el ambos conjuntos pero que no se comparten)
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

# Como determinar si un conjunto es subconjunto de otro
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))   # True. Comprobamos si el conjunto1 es subconjunto del conjunto3
print(conjunto2.issubset(conjunto3))
print(conjunto2.issubset(conjunto1))   # False.

# Como saber si un conjunto es superconjunto de otro
print(conjunto3.issuperset(conjunto1))  # Preguntamos si los elementos del conjunto1 estan dentro del conjunto3
print(conjunto3.issuperset(conjunto2))  # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos: que no comparten ningun elemento en comun
print(conjunto1.isdisjoint(conjunto2))  # True, no hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset   # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni elminar elementos del conjunto.