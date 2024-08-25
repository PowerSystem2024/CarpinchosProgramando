#                           --- Video 1 ---

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']  #Listas | con corchetes
print(nombres)

print(nombres[0])   # Aqui mostramos el elemento 0 de la lista
print(nombres[1])
print(nombres[2])
print(nombres[3])



# Si solo queremos ver el ultimo elemento
print(nombres[-1])  

# Para mostrar el penultimo
print(nombres[-2])

# Es la manera inversa de recorrer los elementos de la lista



#____________________________________________________________________________
#                           --- Video 2 ---

# Recuperar un rango de la lista

print(nombres[0:2])  # solo va a recorrer una cantidad de indices, en este caso
                     # sera el 0 y el 1. No incluye el 2.



# Ir del inicio de la lista al indice (sin incluirlo)

print(nombres[ :3])  # El 'espacio' lo toma como 0, o sea de 0 hacia adelante si incluir el 3



# Desde el indice indicado hasta el final

print(nombres[1: ])   # Ejecuta desde el indice 1 en adelante



# Modificar un valor dentro de la lista

nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)    


# Iterar una lista

for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
    
else:
    print('Se acabaron los elementos de la lista')
    
    
    
#_____________________________________________________________________________
#                       --- Video 3 ---

# Preguntamos cuantos elementes tiene una lista

print(len(nombres))     #'Len' es una funcion, nos dara la cantidad de elementos
                        # que tiene una lista. Debemos pasarle un paramentro (lista)


# Agregamos un elemento

nombres.append('Marcelo')   # Funcion 'append' nos deja agregar un elemento a una lista
print(nombres)              # El elemento agregado se va al final


# Insertar un elemento en un indice especifico

nombres.insert(1, 'Alberto')
print(nombres)              # 'Alberto' se inserto en el indice 1

nombres.insert(3, 'Debora')
print(nombres)              # 'Debora' se inserto en el indice 3


# Eliminarmos un elemento

nombres.remove('Alberto')
print(nombres)              # 'Alberto' se elimino


# Eliminar el ultimo elemento

nombres.pop()
print(nombres)


# Eliminar un indice especifico

del nombres[2]              # 'del' = delete (eliminar)
print(nombres)              # Elimino el elemento 2


# Eliminar, borrar o limpiar todos los elementos

nombres.clear()
print(nombres)


# Eliminar la lista

del nombres
#print(nombres)  # Nos sale un error por que la lista ya ha sido eliminada.