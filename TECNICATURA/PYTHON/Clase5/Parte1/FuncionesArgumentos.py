# Funciones: Argumentos, Variables en Funciones
# Definición de función
# Si se desconoce el número de argumentos que la función recibirá, se utiliza el *, 
# así los argumentos varían
# Normalmente se utiliza *args
def listaNombres(*nombres):
    for nombre in nombres:
        # La variable nombre se convertirá en una tupla
        print(nombre)

# Fuera del bloque, se pasarán los argumentos
# Por más que se impriman en líneas diferentes, los argumentos seguirán agregándose sin problemas
listaNombres('Mercedes', 'Nelson', 'Nicolás', 'Mariana', 'Wanda')
listaNombres('Melina', 'Cirano', 'Ana', 'Ariel', 'Natalia', 'Osvaldo', 'Liliana')
