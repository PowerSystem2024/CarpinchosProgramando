# Lista de elementos con funciones (convertir)
# Distintos tipos de datos como argumentos
# Definición de función (establecimiento tipo lista)
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

# Creación de lista
nombres2 = ['Nelson', 'Mercedes', 'Mariana']
# Llamado a la lista
desplegarNombres(nombres2)

# Este llamado se imprimira de forma que cada uno de los elementos quede en cada renglón. 
# Es decir: 
# A 
# n
# a
desplegarNombres('Ana')

# En caso de llamar un número entero, saltará error a la hora de imprimir, 
# ya que no es un objeto iterable
#   desplegarNombres(10)
# Si se llaman a dos números (o más) enteros, el error persistirá
#   desplegarNombres(10, 11)

# Para recorrer números enteros, hay que transformar en tupla
# Para que sea una tupla con un solo elemento, 
# no hay que olvidar de dejar la coma al lado del mismo ya que sin ella saltará error
desplegarNombres((10, 11))
# Una alternativa a la tupla, es la lista
desplegarNombres([22, 55])
