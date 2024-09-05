# Pilas usando listas
pila = [1, 2, 3,]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
pila.append(6)
print(pila)


# Quitando elmentos por el final
pila.pop()   # Elimina el ultimo elemento de nuestra lista. Este metodo saca y retorna
print(pila)

# Retornamos el elemento borrado
elementoBorrado = pila.pop()
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')