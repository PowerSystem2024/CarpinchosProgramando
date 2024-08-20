#lista = wanda, nico,paula, mercedes, mariana, nelson

nombres =["Wanda", "Nico","Paula","Mercedes","Mariana","Nelson"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[4])
print(nombres[5])
print(nombres[-2])
print(nombres[0:2]) #Solo muestrael el indice 0 , 1 pero no el 2



print (nombres[ :4])
   # Al dejar el espacio vacio damos a entender que queremos solo las 
   # 4 primeras posiciones, por lo tanto se muestra hasta el indice

print (nombres[ 2: ])
   # Al dejar el espacio vacio damos a entender que queremos desde el
   # indice 2 "Paula" hasta el final 

nombres[3] = "Mercedes"
nombres[0] = "Wanda"
print(nombres)

# Iterar una lista
for nombre in nombres:
 print(nombre)
   # Para mostrar los nombres por separado

else: 
 print("Se acabaron los integrantes del grupo carpinchos programando")

# Fin de Listas Parte 2

#  Listas Parte 3



print(len(nombres)) 
   # "len" nos indica la cantidad de elementos que tiene una lista
   # Como parametro le pasamos la lista

nombres.append("Fernando") 
   # "append" sirve paraagregar elementos a una lista 

print(nombres)
   # El elemento se ingresa al final de la lista 

nombres.insert(1,"Javier") 
   # Esta funcion se ejecuta con un entero + el elemento
   # que queremos ingresar a nuestra lista

print(nombres)
   # Corre los otros elementos a la derecha

nombres.insert(3,"Victoria") 
   # Otro ejemplo

print(nombres)
   # Se puede apreciar que "Mercedes" que estaba en la posicion 3
   # y ahora paso a estar en ña posicion 4 agregando a "Victoria"
   # en la posicion 3

nombres.remove("Victoria")
   # Esta funcion Remueve el elemento de la lista que elijamos

print(nombres)

nombres.pop()
   # Esta funcion usado de esta manera remueve el ultimo elemento 
   # de la lista

print(nombres)

del nombres [1]
   # Elimina una posicion "del" significa "delete "(eliminar)

print(nombres)
   # Se elimino el nombre "Javier"

nombres.clear()
   # Elimina/limpia todos los elementos de la lista 

print(nombres)
   # Se borro todo el contenido de "nombres"

del nombres 
   # Eliminamos "nombres"

print(nombres)
   #Salta error de que no esta definida "nombres"
   
# Fin de Listas Parte 3

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3 

print() #Salto de linea 
print("Rango de numeros entre 0 y 10 divisibles entre 3")
print() #Salto de linea 

for i in range(1,11):
 if i % 3 == 0:
  print(i)

# Fin Ejercicio 1

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimelos 

print() #Salto de linea 
print("Rango con valores inicio = 2 y fin = 6")
print() #Salto de linea 

for i in range(2,7):
 print(i)

# Fin Ejercicio 2

# Ejercicio 3

print() #Salto de linea 
print("Rango con valores de inicio = 3, fin = 10, incremento = 2") 
print() #Salto de linea 

for i in range(3,11,2):
 print(i)

print() #Salto de linea 

 # Fin Ejercicio 3
#--------------------------------------------

 # Definimos una tupla 

cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))

# Para acceder a un elemento usamos corchetes, no parentesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina [0:2])

   # Muestra solo "Cuchara" y "cuchillo"  porque muestra el 
   # elemento "0" y "1", al 2 no llega 

# Ejemplo de cadena 
verduras = ("papa")

print(verduras)

# Diferencia entre cadena y tupla al imprimir 
# ('cuchara',) = tupla
# papa = cadena 

verduras = ("papa",)
# Pasa a ser tupla, porque necesita aunque sea de un elemento: la coma
# De lo contrario, solo pasaria a ser un tipo str cadena

print(verduras)

#Recorremos los elementos de la tupla 
for cocinar in cocina:
 print(cocinar) # print esta usando /n para saltos de lineas 

for cocinar in cocina:
  print(cocinar, end=" ") # Print finaliza los saltos de linea al usar: (end=" ")


#  cocina[0] = "plato"
#   print(cocina) 

# Salta error porque en las tuplas no se pueden modificar los elementos

cocinarLista = list(cocina)
cocinarLista[0] = "Plato"
cocina = tuple(cocinarLista)
print("\n",cocina) # Print reanuda los saltos de linea con ("\n",)

#NO ES BUENO HACER ESTA CONVERSION DE TUPLA A LISTA Y DE LISTA A TUPLA

# No se puede utilizar en tuplas:

# .append 
# .insert
# .remove


   # del cocina
# Elimina la tupla


# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5
# e imprimir por consola [1,3,2]
# Creamos una lista que solo incluya los números menores a 5
lista = []

for num in tupla:
     if num < 5:
          lista.append(num)


# Imprimimos la lista 
print(lista)