conjunto = set() # La unica forma de inicializar un conjunto vacío y poder agregar elementos despues, es con set().
conjunto1 = {"bye"} # Si el conjunto se inicializa vacio {} no se puede modificar.
conjunto.add(7) # con la funcion add se puede agregar solamente un elemento.
conjunto.add("Hola") # Agregamos a conjunto, un elemento.
print(conjunto)
conjunto1.add("Hola") # Agregamos a conjunto1 un elemento.
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el nro 3 está en el conjunto.

# Como comparar dos conjuntos
print(conjunto1 == conjunto) # Nos devuelve un booleano.