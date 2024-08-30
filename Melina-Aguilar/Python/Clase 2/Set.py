# COLECCIONES
# 1. Listas []: mantiene un orden y se puede modificar, es decir es mutable
# 2. Tuplas (): mantiene un orden y NO se puede modificar.
# 3. Set {}: no tiene un orden, no permite almacer elementos duplicados o repetidos
#         no se puede modificar, pero si se puede agregar o eliminar.
#         no mantiene ningun indice, es decir, que cuando accedemos al tipo set o 
#         imprimimos el orden es aleatorio, por que no hay indice para ordenar los elementos.
#         No tiene orden, no tiene indice.


#Tipo set (o conjuntos)

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas) # Los muestra en orden aleatorios cada vez.

planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))


# Revisar  si un elemento existe dentro de set
print('Marte' in planetas) # True - Nos devuelve un tipo booleano. Es una pregunta. "Marte esta en 'planetas'?"
print('Júpiter' in planetas) # respeta acentos, mayus y minus.

print('Júpiter' not in planetas)


# Agregar un elemento
planetas.add('Tierra')  # 'add' es una funcion para añadir.
planetas.add('Tierra')  # no añade un elemento duplicado.
print(planetas)


# Sirve para evitar elementos duplicados en una lista de datos.


# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')
print(planetas)

planetas.discard('Tierra')  # Si nos equivocamos al escribir con 'discard', no pasa nada, tampoco se borra.
print(planetas)


# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas 