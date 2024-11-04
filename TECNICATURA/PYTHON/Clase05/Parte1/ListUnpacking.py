# List Unpacking: Desempaquetado de listas
# Creación de una función con dos parámetros
def show(name, lastname):
    print(name + " " + lastname)

# Creación de una lista con nombres
persona = ['Ana', 'Garín']

# FORMAS DE PASAR POR LOS DATOS
# Se pasa por cada dato de la lista (uno por uno) directamente a la función
show(persona[0], persona[1])

# A diferencia del anterior, se pasa todo junto
show(*persona)

# Estos procesos se pueden realizar también para las tuplas
persona2 = ('Nelson', 'Ríos')
show(*persona2)

# También, se pueden realizar para diccionarios
persona3 = {
    'lastname': 'Atim', 'name': 'Mercedes'
}

# Para los diccionarios es necesario poner dos asteriscos, uno para clave y otro para valor
show(**persona3)
